#!/bin/sh

#docker stack rm shopiflag

docker build -t shopiflag_web ./shopiflag_web

docker build -t httpbots ./httpbots

docker build -t botnet ./botnet

#docker swarm init --advertise-addr=127.0.0.1
#docker stack deploy -c docker-compose.yml shopiflag
docker-compose up -d
# useful commands:
# docker stack rm shopiflag
# sudo docker service logs shopiflag_httpbots
# sudo docker ps
# sudo docker exec -i -t cf3b637c261f /bin/bash
