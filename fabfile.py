from fabric.api import task, run, put, sudo, cd, env, get
from fabric.contrib.files import exists


env.use_ssh_config = True


@task
def bootstrap_salt(env='production'):
    run("curl -L https://bootstrap.saltstack.com | sudo sh -s -- -P git v2015.8.2")
    conf = 'salt.conf'
    if env == 'staging':
        conf = 'salt-staging.conf'
    elif env == 'production':
        conf = 'salt-production.conf'
    else:
        raise ValueError("Unrecognized environment: {}".format(env))
    put(conf, '/etc/salt/minion', use_sudo=True)


@task
def bootstrap_project(target='wagtail'):
    put("pillar/deploy_rsa", "/root/.ssh/id_rsa",
        use_sudo=True, mode=0400)
    with cd("/root/"):
        if not exists('/root/littleweaverweb.com'):
            sudo("git clone git@github.com:littleweaver/littleweaverweb.com.git")
        with cd('littleweaverweb.com'):
            sudo('git fetch')
            sudo('git reset --hard origin/{}'.format(target))
            if not exists('/srv/salt'):
                sudo('mkdir /srv/salt')
            sudo("cp -R salt/* /srv/salt")


@task
def put_pillar():
    if not exists('/srv/pillar'):
        sudo('mkdir /srv/pillar')
    put("pillar/*", "/srv/pillar", use_sudo=True)


@task
def get_pillar():
    get("/srv/pillar/*", "pillar/")


@task
def run_management_command(command):
    full_command = "/bin/bash -l -c 'source /var/www/env/bin/activate && python /var/www/project/manage.py {0}'".format(command)
    sudo(full_command, user="webproject")


@task
def salt_call():
    sudo("salt-call --local state.highstate")


@task
def full_deploy(env, target='master'):
    bootstrap_salt(env)
    bootstrap_project(target)
    salt_call()
