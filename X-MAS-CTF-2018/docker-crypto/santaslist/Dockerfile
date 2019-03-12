FROM python:3.6-stretch
RUN apt-get update
RUN apt-get install xinetd -y
RUN apt-get install nmap -y
RUN apt-get install socat -y
RUN pip3 install pycrypto

COPY files/ /chall
COPY santas_list /etc/xinetd.d/santas_list
RUN /etc/init.d/xinetd restart
WORKDIR /chall
RUN chmod +x server.py
#CMD ["ncat", "-lkvp", "2000", "-e", "/usr/local/bin/python3 /chall/server.py"]
CMD ["socat", "TCP-LISTEN:2000,reuseaddr,fork", "EXEC:'/usr/local/bin/python3 /chall/server.py'"]
