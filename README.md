ksp-ckan
========

This repository contains a script that can take an
imgur gallery and create a [CKAN](https://github.com/KSP-CKAN/CKAN) compatible mod description. 

See an [example](ckan/KSPAssortedFlags.ckan) of an assorted flags pack generated from the following command.

```
./imgur.py http://imgur.com/a/rRUZp ckan/KSPAssortedFlags.ckan \
           --author crzysdrs noaceulemans \
           --modname "KSP Assorted Flags" \
           --desc "162 Flags for KSP"
```