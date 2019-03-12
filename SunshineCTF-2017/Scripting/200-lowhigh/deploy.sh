#!/bin/bash

# Rebuild docker image
docker build -t lowhigh .

# Kill running docker container and remove it
docker rm -f lowhigh >/dev/null 2>&1

# Spawn new running docker container
docker run --restart=unless-stopped --name lowhigh --read-only -itd -v /etc/localtime:/etc/localtime:ro -p 30002:30002 lowhigh
