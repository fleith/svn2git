#!/usr/bin/python3

import subprocess

#TODO: search path recursively
with open("svnexternals.txt", "r") as f:
    for line in f:
        try:
            subprocess.check_call('svn co {0}'.format(line), shell=True)
        except CalledProcessError:
            subprocess.check_call('svn sw {0}'.format(line), shell=True)

