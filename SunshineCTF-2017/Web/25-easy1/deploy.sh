#!/bin/bash

docker build -t easy1 .
docker rm -f easy1 >/dev/null 2>&1
docker run --restart=unless-stopped --name easy1 -itd -v /etc/localtime:/etc/localtime:ro -p 127.0.0.1:5000:80 easy1
