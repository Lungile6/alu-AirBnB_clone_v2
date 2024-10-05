#!/usr/bin/python3
<<<<<<< HEAD
"""
Fabric script based on the file 1-pack_web_static.py that distributes an
archive to the web servers
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['54.234.151.70', '3.87.86.63']


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False
=======
"""Deploy web static to different servers"""
import re
from fabric.context_managers import cd
from fabric.api import env, put, run, sudo
from os.path import join, exists, splitext


env.user = "ubuntu"
env.hosts = ["54.221.62.39", "44.223.30.163"]
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """
    Deploy a compressed archive to a remote server.
    Args:
        archive_path (str): The path to the compressed archive.
    Returns:
        bool: True if the deployment is successful, False otherwise.
    """

    if not exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")
        file_name = re.search(r'[^/]+$', archive_path).group(0)
        deploy_path = join("/data/web_static/releases/",
                           splitext(file_name)[0])
        sudo("mkdir -p {}".format(deploy_path))

        sudo("tar -xzf /tmp/{} -C {}".format(file_name, deploy_path))

        with cd(deploy_path):
            sudo("mv web_static/* .")
            sudo("rm -rf web_static")

        sudo("rm /tmp/{}".format(file_name))
        sudo("rm -rf /data/web_static/current")

        sudo('ln -sf {} /data/web_static/current'.format(deploy_path))
    except Exception as err:
        return False

    return True
>>>>>>> 1a1dd196b0890378b3a78d8ddc78d7914dccd33f
