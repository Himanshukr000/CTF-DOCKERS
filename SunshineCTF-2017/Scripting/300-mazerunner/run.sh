#!/bin/bash

socat tcp4-l:30003,reuseaddr,fork EXEC:"python server.py",pty,ctty,echo=0
# socat -v tcp4-l:30003,reuseaddr,fork EXEC:"./mazechall.py",pty,ctty,echo=0
