#!/bin/bash

# This one is used first

# compile
python -m compileall ./dangerzone.py

# decompile
uncompyle6 ./dangerzone.pyc
