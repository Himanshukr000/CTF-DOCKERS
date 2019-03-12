#!/bin/bash

gcc -m32 -fstack-protector-all -mpreferred-stack-boundary=2 -no-pie ./timber.c -o timber
