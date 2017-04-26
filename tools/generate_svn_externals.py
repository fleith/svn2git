#!/usr/local/bin/python3

import sys
import subprocess
import xml.etree.ElementTree as ET

path_to_search = sys.argv[1] if len(sys.argv) > 1 else "."

svnexternals = subprocess.run("svn pg --xml svn:externals -R {0}".format(path_to_search), shell=True, check=True, stdout=subprocess.PIPE)

root = ET.fromstring(svnexternals.stdout)

for child in root:
    path = child.attrib['path']
    for other in child:
        if 'svn:externals' in other.attrib['name']:
            print('writing svnexternals.txt to {0}'.format(path))
            f = open('{0}/svnexternals.txt'.format(path), 'w')
            f.write(other.text)

