#!/usr/bin/env python3

import sys
import subprocess
import xml.etree.ElementTree as ET

path_to_search = sys.argv[1] if len(sys.argv) > 1 else "."

svn_externals = subprocess.run("svn pg --xml svn:externals -R {0}".format(path_to_search), shell=True, check=True,
                               stdout=subprocess.PIPE)

root = ET.fromstring(svn_externals.stdout)


# Normalize svn externals definition format (format was changed after svn version 1.5)
def normalize_external(external):
    elements = external.split(' ')
    uri = [ind for ind, element in enumerate(elements) if ':' in element]
    if len(uri) == 1:
        elements.insert(0, elements.pop(uri[0]))
        return " ".join(elements)
    return external


for child in root:
    path = child.attrib['path']
    for other in child:
        if 'svn:externals' in other.attrib['name']:
            print('writing svnexternals.txt to {0}'.format(path))
            f = open('{0}/svnexternals.txt'.format(path), 'w')
            externals = other.text.strip().split('\n')
            normalized_externals = [normalize_external(x) for x in externals]
            f.write("\n".join(normalized_externals))
