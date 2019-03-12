#!/bin/bash

docker build -t easy2 .
docker rm -f easy2 >/dev/null 2>&1
docker run --restart=unless-stopped --name easy2 -itd -v /etc/localtime:/etc/localtime:ro -p 127.0.0.1:5001:80 easy2
