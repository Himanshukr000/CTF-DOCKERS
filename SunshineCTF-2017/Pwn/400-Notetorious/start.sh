#!/bin/bash

socat TCP-LISTEN:20003,fork,reuseaddr EXEC:"./login.py",su=notetorious_auth,pty,ctty,echo=0,stderr
