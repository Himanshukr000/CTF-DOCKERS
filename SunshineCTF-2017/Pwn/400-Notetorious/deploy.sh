#!/bin/bash

# Rebuild docker image
docker build -t notetorious .

# Kill running docker container and remove it
docker rm -f notetorious >/dev/null 2>&1

# Spawn new running docker container
docker run --restart=unless-stopped --name notetorious -itd -v /etc/localtime:/etc/localtime:ro -p 20003:20003 notetorious
