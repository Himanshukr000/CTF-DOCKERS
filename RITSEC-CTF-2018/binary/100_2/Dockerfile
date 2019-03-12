FROM ubuntu:16.04

RUN useradd -s /bin/bash -m -d /home/pwn3user pwn3user
WORKDIR /home/pwn3user

RUN apt-get update && \
    apt-get -y install socat libc6-dev-i386

ADD ./dist/pwn3 /home/pwn3user/pwn3
RUN chown pwn3user:pwn3user /home/pwn3user/pwn3
RUN chmod +x /home/pwn3user/pwn3

ADD ./deploy/flag.txt /home/pwn3user/flag.txt
RUN chown pwn3user:pwn3user /home/pwn3user/flag.txt

USER pwn3user

CMD socat TCP-LISTEN:1338,reuseaddr,fork EXEC:"/home/pwn3user/pwn3"