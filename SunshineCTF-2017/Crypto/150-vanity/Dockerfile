FROM python:2.7

RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y socat && \
	pip install pycrypto

WORKDIR /chall
COPY src/ .

CMD ./run.sh
