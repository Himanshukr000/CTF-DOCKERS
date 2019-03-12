#!/bin/bash

docker images | grep pwn3 >/dev/null 2>&1

if [ "$?" != "0" ]; then
    docker build . -t pwn3
fi

docker ps -a | grep pwn3_1 >/dev/null 2>&1

if [ "$?" == "0" ]; then
    docker stop pwn3_1 >/dev/null 2>&1
    docker rm pwn3_1 >/dev/null 2>&1
fi

docker run --read-only --user 1000 -tid --name pwn3_1 -p 1338:1338 pwn3