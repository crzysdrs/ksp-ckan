#!/bin/bash
ZIP_PATH=$1
echo '{
    "spec_version": 1,
    "identifier"  : "<ImgurFlags>",
    "name"        : "<ImgurFlags>",
    "author"      : "<AUTHOR",
    "version"     : "0.1",
    "abstract"    : "",
    "ksp_version" : "any",
    "license"     : "GPL-3.0",
    "download"    : "<IMGUR ZIP URL>",
    "license": "CC-BY",
    "resources" : {
        "homepage" : "<IMGUR GALLERY URL>"
    },
    "install": ['

IFS=$(echo -en "\n\b")
FILES=`ls ${ZIP_PATH}`

for n in $FILES; do
    echo '    {'
    echo '        "file":"'$n'",'
    echo '        "install_to":"GameData/Squad/Flags/"'
    echo '    },'
done

echo ']
}'

