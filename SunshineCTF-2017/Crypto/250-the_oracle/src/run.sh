#!/bin/bash

socat tcp4-l:40002,reuseaddr,fork EXEC:"python server.py",pty,ctty,echo=0
# socat -v tcp4-l:40002,reuseaddr,fork exec:"python server.py",pty,ctty,echo=0
