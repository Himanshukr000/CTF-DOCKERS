#!/bin/sh

LIB="$(shuf -n1 -e libs/*)"
LD_PRELOAD="${LIB}" ./main
