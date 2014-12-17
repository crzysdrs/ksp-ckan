#!/usr/bin/env python3
import json
import urllib.request
import zipfile
import argparse
import sys

parser = argparse.ArgumentParser(description='Convert Imgur Gallery into a CKAN Flags Description.')
parser.add_argument('imgur_url', help='imgur URL')
parser.add_argument('ckan_file', nargs='?', type=argparse.FileType('w'), help='ckan output file', default=sys.stdout)
parser.add_argument('--author', help='author name', default='Your Name Here')
parser.add_argument('--modname', help='mod name', default='Unnamed Flag Mod')
parser.add_argument('--desc', help='description', default='Undescribed Flag Mod')
args = parser.parse_args();

ckan = {
    'spec_version':1,
    'identifier':args.modname.replace(" ", ""),
    'name':args.modname,
    'author':args.author,
    'version':'0.1',
    'abstract':args.desc,
    'ksp_version':'any',
}

ckan['resources'] = {'homepage':args.imgur_url}
file_name, headers = urllib.request.urlretrieve(args.imgur_url + '/zip')

imgur_zip = zipfile.ZipFile(file_name, 'r')
install_steps = []
for i in imgur_zip.namelist():
    step = {
        'file':i,
        'install_to':'GameData/Squad/Flags',
    }
    install_steps.append(step)

ckan['install'] = install_steps

json.dump(ckan, args.ckan_file, indent=1, sort_keys=True)
    

