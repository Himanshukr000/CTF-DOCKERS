#!/bin/bash

# Rebuild docker image
docker build -t mazerunner .

# Kill running docker container and remove it
docker rm -f mazerunner >/dev/null 2>&1

# Spawn new running docker container
docker run --restart=unless-stopped --name mazerunner --read-only -itd -v /etc/localtime:/etc/localtime:ro -p 30003:30003 mazerunner
