FROM ubuntu:latest

# Install utilities
RUN apt-get update --fix-missing && apt-get -y upgrade &&\
apt-get install -y sudo curl wget unzip git

# Install node 6
RUN curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash - &&\
sudo apt-get install -y nodejs

# install chromium-browser
RUN sudo apt-get update
RUN apt-get install chromium-browser -y

WORKDIR /csrf
COPY bots           /csrf/bots
COPY run.sh         ./
COPY package.json   ./

RUN npm install

ENV LIGHTHOUSE_CHROMIUM_PATH /usr/bin/chromium-browser

CMD ./run.sh