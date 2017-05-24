#!/usr/local/bin/python3

import sys
import glob
import subprocess

path_to_search = sys.argv[1] if len(sys.argv) > 1 else "."


def svn_co_or_sw(path):
    with open(path, "r") as f:
        for line in f:
            try:
                subprocess.check_call('svn co {0}'.format(line), shell=True)
            except subprocess.CalledProcessError:
                subprocess.check_call('svn sw {0}'.format(line), shell=True)


for filename in glob.iglob('{0}/**/svnexternals.txt'.format(path_to_search), recursive=True):
    svn_co_or_sw(filename)
