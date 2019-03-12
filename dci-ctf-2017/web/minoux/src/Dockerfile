FROM ubuntu:16.04

RUN apt-get update && apt-get -y dist-upgrade
RUN apt-get install -y nodejs npm redis-server

COPY ./minoux /minoux

WORKDIR /minoux

RUN npm install

CMD ./start.sh