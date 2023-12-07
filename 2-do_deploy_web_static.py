#!/usr/bin/python3
"""Fabric script that distributes an archive to your web server
 using the function deploy"""

from fabric.api import *
from os import path
from datetime import datetime

env.hosts = ['100.25.191.187', '54.198.64.165']


def do_pack():
    """A function that compresses the files in web_static folder
    into an archive before they can be sent """

    local("mkdir -p versions")

    current_dt = datetime.now()
    time_stamp = current_dt.strftime("%Y%m%d%H%M%S")
    archive_file = "web_static_{}.tgz".format(time_stamp)
    archive_path = "versions/{}".format(archive_file)

    compress_result = local("tar -cvzf {} web_static".format(archive_path))

    if compress_result.succeeded:
        return archive_path
    else:
        return None


def do_deploy(archive_path):
    """Fabric script that distributes a compressed  archive to
    web servers"""

    if path.exists(archive_path):

        archive = archive_path.split('/')[1]

        # Defining paths for the archive on the server
        ra_path = "/tmp/{}".format(archive)
        r_folder = archive.split('.')[0]
        rd_path = "/data/web_static/releases/{}/".format(r_folder)

        # Uploading the archive into the web server
        put(archive_path, ra_path)

        run("mkdir -p {}".format(rd_path))
        run("tar -xzf {} -C {}".format(ra_path, rd_path))

        # Removing the no longer needed uploaded archive
        run("rm {}".format(ra_path))

        # Moving contents from web_static subfolder to deployment folder
        run("mv -f {}web_static/* {}".format(rd_path, rd_path))

        # removing the empty web_static subfolder
        run("rm -rf {}web_static".format(rd_path))
        run("rm -rf /data/web_static/current")

        # Creating a new symbolic link to the latest version of code
        run("ln -s {} /data/web_static/current".format(rd_path))

        return True

    return False
