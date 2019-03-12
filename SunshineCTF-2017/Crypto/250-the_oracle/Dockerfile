FROM python:2.7
RUN apt-get update && apt-get install -y socat && pip install pycrypto
RUN mkdir /chall
COPY src/ /chall
WORKDIR /chall
CMD ./run.sh
