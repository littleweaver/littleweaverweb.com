include:
  - circus
  - database

app-pkgs:
  pkg.installed:
    - names:
      - git
      - python-virtualenv
      - python-dev
      - gcc
      - libjpeg8-dev
      - libpq-dev
      - ruby
      - ruby-dev

bootstrap_sass:
  gem.installed:
    - name: bootstrap-sass
    - version: 3.3.4.1
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
      - gem: bootstrap_sass

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
    - require:
        - pkg: nginx

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


collectstatic:
  cmd.run:
    - name: {{ pillar['files']['env_dir'] }}bin/python {{ pillar['files']['project_dir'] }}manage.py collectstatic --noinput
    - user: webproject
    - require:
      - file: webproject_project
      - virtualenv: webproject_env
      - postgres_database: webproject_db
      - user: webproject_user

migrate:
  cmd.run:
    - name: {{ pillar['files']['env_dir'] }}bin/python {{ pillar['files']['project_dir'] }}manage.py migrate --noinput
    - user: webproject
    - require:
      - file: webproject_project
      - virtualenv: webproject_env
      - postgres_database: webproject_db
      - user: webproject_user

compress:
  cmd.run:
    - name: {{ pillar['files']['env_dir'] }}bin/python {{ pillar['files']['project_dir'] }}manage.py compress
    - user: webproject
    - require:
      - user: webproject_user
      - file: webproject_project
      - virtualenv: webproject_env
      - pip: project
