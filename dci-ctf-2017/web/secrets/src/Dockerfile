FROM ubuntu:latest
FROM zenato/puppeteer

COPY ./secrets /opt/secrets

WORKDIR /opt/secrets

RUN npm install

CMD node server.js
