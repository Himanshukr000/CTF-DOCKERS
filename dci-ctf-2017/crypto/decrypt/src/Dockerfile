FROM ubuntu:16.04

RUN apt-get update && apt-get -y dist-upgrade
RUN apt-get install -y python python-pip socat

RUN pip install pycrypto

COPY ./service.py /opt/service.py
COPY ./flag /opt/flag

WORKDIR /opt

CMD socat -d -d TCP-LISTEN:4242,reuseaddr,fork,su=nobody EXEC:/opt/service.py
