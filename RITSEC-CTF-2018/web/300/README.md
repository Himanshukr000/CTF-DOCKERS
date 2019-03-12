# Web C: Archivr
**Author**: jwood

**Flag**: RITSEC{uns3r1al1z3_4LL_th3_th1ng5}

## Description
_None_

## Deployment
An Apache webserver with PHP (`mod_php`) is required for this challenge (versions _probably_ don't matter). The contents of [`challenge.zip`](./challenge.zip) should be extracted to the webserver root directory. Ensure the zip is not left accessible.

The webserver user (`www-data`) must be given write access to the `uploads/` directory (included in [`challenge.zip`](./challenge.zip)).

**This challenge allows users to list directory contents on the webserver. If any other challenges are hosted on the same server, permissions must be set appropriately.**

Users must be provided the webserver URL.

## Writeup
The writeup directory contains the following files:
- [`writeup.docx`](./writeup/writeup.docx): A description of how the challenge would be solved
- [`payload.phar`](./writeup/payload.phar): An example exploit payload
