import os

from fabric.api import task, run, put, sudo, cd, env, get
from fabric.contrib.files import exists


env.use_ssh_config = True
REPO_SLUG = 'littleweaverweb.com'
REPO_URL = "https://github.com/littleweaver/" + REPO_SLUG + ".git"
DEFAULT_BRANCH = 'wagtail'
CURRENT_DIR = os.path.dirname(__file__)


@task
def install_salt():
    run("curl -L https://bootstrap.saltstack.com | sudo sh -s -- -P git a6c0907")


@task
def put_pillar():
    if not exists('/srv/pillar'):
        sudo('mkdir /srv/pillar')
    put("pillar/*", "/srv/pillar", use_sudo=True)


@task
def get_pillar():
    get("/srv/pillar/*", "pillar/%(path)s")


@task
def deploy_code(branch_or_commit=DEFAULT_BRANCH):
    put("pillar/deploy_rsa", "/root/.ssh/id_rsa",
        use_sudo=True, mode=0400)
    with cd("/var/www/"):
        project_dir = "/var/www/{}".format(REPO_SLUG)
        if not exists(project_dir):
            sudo("git clone {}".format(REPO_URL))
        with cd(REPO_SLUG):
            sudo('git fetch')
            sudo('git stash')
            sudo('git checkout {}'.format(branch_or_commit))
            sudo('git reset --hard origin/{}'.format(branch_or_commit))
            sudo('chmod -R a+rw {}'.format(project_dir))
            sudo('rm -rf /srv/salt')
            sudo('mkdir /srv/salt')
            sudo("cp -R salt/* /srv/salt")


@task
def salt_call():
    sudo("salt-call --local state.highstate")


@task
def deploy(branch_or_commit=DEFAULT_BRANCH):
    if not run('which salt-call', quiet=True):
        install_salt()
    if not os.path.exists(os.path.join(CURRENT_DIR, 'pillar')):
        get_pillar()
    deploy_code(branch_or_commit)
    salt_call()
    manage('migrate --noinput')
    manage('collectstatic --noinput')
    manage('compress --noinput')


@task
def manage(command):
    full_command = "/bin/bash -l -c 'source /var/www/env/bin/activate && python /var/www/project/manage.py {0}'".format(command)
    sudo(full_command, user="webproject")


@task
def restart_gunicorn():
    sudo('circusctl restart gunicorn')
