#!/bin/bash

# Rebuild docker image
docker build -t falloutcomrade .

# Kill running docker container and remove it
docker rm -f falloutcomrade >/dev/null 2>&1

# Spawn new running docker container
docker run --restart=unless-stopped --name falloutcomrade --read-only -itd -v /etc/localtime:/etc/localtime:ro -p 30001:30001 falloutcomrade
