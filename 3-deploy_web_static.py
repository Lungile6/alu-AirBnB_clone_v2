#!/usr/bin/python3
<<<<<<< HEAD
"""
Fabric script based on the file 2-do_deploy_web_static.py that creates and
distributes an archive to the web servers

execute: fab -f 3-deploy_web_static.py deploy -i ~/.ssh/id_rsa -u ubuntu
"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir
env.hosts = ['54.234.151.70', '3.87.86.63']


def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
=======
import re
from time import strftime
from fabric.context_managers import cd
from fabric.api import env, put, sudo, local
from os.path import join, exists, splitext

env.hosts = ["54.221.62.39", "44.223.30.163"]


def do_pack():
    """
    Generates a .tgz file from the contents of the web_static folder

    Returns:
        str: The file path of the generated .tgz file if successful else None.
    """

    date_time = strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(date_time)
    try:
        local("mkdir -p versions")
        local("tar -zcvf {} web_static".format(file_name))
        return file_name
    except Exception as err:
>>>>>>> 1a1dd196b0890378b3a78d8ddc78d7914dccd33f
        return None


def do_deploy(archive_path):
<<<<<<< HEAD
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


def deploy():
    """creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
=======
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


def deploy():
    """
    Deploys the web_static content to the web servers.
    """
    archive_path = do_pack()
    if not archive_path:
>>>>>>> 1a1dd196b0890378b3a78d8ddc78d7914dccd33f
        return False
    return do_deploy(archive_path)
