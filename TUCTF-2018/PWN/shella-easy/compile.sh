#!/bin/bash

gcc -m32 -no-pie -z execstack -mpreferred-stack-boundary=2 ./shella-easy.c -o shella-easy
