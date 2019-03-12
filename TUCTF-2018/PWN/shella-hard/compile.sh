#!/bin/bash

gcc -m32 -fno-pic -no-pie -mpreferred-stack-boundary=2 ./shella-hard.c -o shella-hard
