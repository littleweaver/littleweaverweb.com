include:
  - circus
  - database

nodejs.ppa:
  pkg.installed:
    - name: apt-transport-https
  pkgrepo.managed:
    - humanname: NodeSource Node.js Repository
    - name: deb {{ salt['pillar.get']('node:ppa:repository_url', 'https://deb.nodesource.com/node_0.12') }} {{ grains['oscodename'] }} main
    - dist: {{ grains['oscodename'] }}
    - file: /etc/apt/sources.list.d/nodesource.list
    - key_url: https://deb.nodesource.com/gpgkey/nodesource.gpg.key
    - require:
      - pkg: nodejs.ppa

app-pkgs:
  pkg.installed:
    - names:
      - git
      - python-virtualenv
      - python-dev
      - gcc
      - libjpeg8-dev
      - libpq-dev
      - imagemagick
      - nodejs
      - nodejs-legacy
      - npm
    - require:
      - pkgrepo: nodejs.ppa

autoprefixer-pkgs:
  npm.installed:
    - pkgs:
      - postcss-cli
      - autoprefixer
    - require:
      - pkg: app-pkgs

webproject_user:
  user.present:
    - name: webproject
    - gid_from_name: True

webproject_dirs:
  file.directory:
    - user: webproject
    - group: webproject
    - makedirs: true
    - names:
      - {{ pillar['files']['root_dir'] }}
      - {{ pillar['files']['media_dir'] }}
      - {{ pillar['files']['static_dir'] }}
    - require:
      - user: webproject

webproject_env:
  virtualenv.managed:
    - name: {{ pillar['files']['env_dir'] }}
    - requirements: {{ pillar['files']['clone_dir'] }}requirements.txt
    - system_site_packages: false
    - no_deps: true
    - clear: false
    - user: webproject
    - require:
      - pkg: app-pkgs
      - user: webproject
      - file: webproject_dirs
      - npm: autoprefixer-pkgs

project:
  pip.installed:
    - editable: {{ pillar['files']['clone_dir'] }}
    - bin_env: {{ pillar['files']['env_dir'] }}
    - user: webproject
    - require:
      - virtualenv: webproject_env

newrelic_pip:
  pip.installed:
    - name: newrelic==2.54.0.41
    - bin_env: {{ pillar['files']['env_dir'] }}
    - user: webproject
    - require:
      - virtualenv: webproject_env

django_log_dir:
  file.directory:
    - name: {{ pillar['files']['logs']['django_dir'] }}
    - user: webproject
    - group: webproject
    - mode: 755

webproject_project:
  file.recurse:
    - user: webproject
    - group: webproject
    - name: {{ pillar['files']['project_dir'] }}
    - source: salt://webserver/webproject/
    - template: jinja
    - require:
      - file: django_log_dir
      - virtualenv: {{ pillar['files']['env_dir'] }}
      - pip: project
      - pip: newrelic_pip
      - service: postgresql

nginx:
  user:
    - present
  pkg:
    - latest
  service:
    - running
    - watch:
      - file: nginx_conf
    - require_in:
        - file: letsencrypt-config
    - require:
        - pkg: nginx


nginx-restart-cron:
  cron.present:
    - name: service nginx restart
    - month: '*'
    - minute: random
    - hour: random
    - day: random
    - identifier: nginx-restart-cron
    - require:
      - service: nginx

nginx_conf:
  file.managed:
    - name: /etc/nginx/sites-available/default
    - source: salt://webserver/nginx.conf
    - template: jinja
    - makedirs: True
    - mode: 755
    - user: nginx
    - group: nginx
    - require:
      - pkg: nginx

letsencrypt_webroot_dir:
  file.directory:
    - user: nginx
    - group: nginx
    - makedirs: true
    - name: {{ pillar['letsencrypt']['webroot_dir'] }}
    - require:
      - pkg: nginx

eventlet:
  pip.installed:
    - bin_env: {{ pillar['files']['env_dir'] }}
    - user: webproject
    - require:
      - virtualenv: webproject_env

gunicorn:
  pip.installed:
    - name: gunicorn==19.1.1
    - bin_env: {{ pillar['files']['env_dir'] }}
    - user: webproject
    - require:
      - virtualenv: webproject_env
      - pip: eventlet

gunicorn_log:
  file.managed:
    - name: {{ pillar['files']['logs']['gunicorn'] }}
    - user: webproject
    - group: webproject
    - mode: 644
    - require:
      - pip: gunicorn

gunicorn_circus:
  file.managed:
    - name: /etc/circus.d/gunicorn.ini
    - source: salt://webserver/gunicorn.ini
    - makedirs: True
    - template: jinja
    - require:
      - file: gunicorn_log
      - user: webproject_user
      - virtualenv: webproject_env
    - watch_in:
      - service: circusd

gunicorn_circus_restart:
  cmd.run:
    - name: circusctl restart gunicorn
    - require:
      - file: webproject_project
      - file: gunicorn_circus
      - virtualenv: webproject_env
      - service: circusd
