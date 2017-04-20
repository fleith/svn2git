#!/usr/local/bin/python3

import subprocess
import xml.etree.ElementTree as ET

#TODO: get initial path for svn pg --xml svn::externals -R from args
svnexternals = subprocess.run("svn pg --xml svn:externals -R .", shell=True, check=True, stdout=subprocess.PIPE)

#tree = ET.parse('externals.xml')
#root = tree.getroot()
root = ET.fromstring(svnexternals.stdout)

for child in root:
    print(child.tag, child.attrib)
    for other in child:
        print(other.tag, other.attrib, other.text)

