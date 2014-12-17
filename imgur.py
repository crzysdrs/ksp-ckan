#!/usr/bin/env python3
import json
import urllib.request
import zipfile
import argparse
import sys
from collections import OrderedDict

parser = argparse.ArgumentParser(description='Convert Imgur Gallery into a CKAN Flags Description.')
parser.add_argument('--author', help='author name', nargs='*', default=['Your Name Here'])
parser.add_argument('--modname', help='mod name', default='Unnamed Flag Mod')
parser.add_argument('--desc', help='description', default='Undescribed Flag Mod')
parser.add_argument('imgur_url', help='imgur URL')
parser.add_argument('ckan_file', nargs='?', type=argparse.FileType('w'), help='ckan output file', default=sys.stdout)

args = parser.parse_args();

ckan = OrderedDict(
    [
        ('spec_version', 1),
        ('identifier', args.modname.replace(" ", "")),
        ('name', args.modname),
        ('author', args.author),
        ('version', '0.1'),
        ('abstract', args.desc),
        ('ksp_version', 'any'),
    ]
)

ckan['resources'] = {'homepage':args.imgur_url}
ckan['download'] = args.imgur_url + '/zip'
file_name, headers = urllib.request.urlretrieve(ckan['download'])

imgur_zip = zipfile.ZipFile(file_name, 'r')
install_steps = []
for i in sorted(imgur_zip.namelist()):
    step = OrderedDict([
        ('file', i),
        ('install_to','GameData/Squad/Flags'),
    ])
    install_steps.append(step)

ckan['install'] = install_steps

json.dump(ckan, args.ckan_file, indent=1)
    

