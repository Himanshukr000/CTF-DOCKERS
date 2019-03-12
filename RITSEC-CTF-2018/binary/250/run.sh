#!/bin/bash

docker images | grep pwn2 >/dev/null 2>&1

if [ "$?" != "0" ]; then
    docker build . -t pwn2
fi

docker ps -a | grep pwn2_1 >/dev/null 2>&1

if [ "$?" == "0" ]; then
    docker stop pwn2_1 >/dev/null 2>&1
    docker rm pwn2_1 >/dev/null 2>&1
fi

docker run --user 1000 -tid --name pwn2_1 -p 1337:1337 pwn2