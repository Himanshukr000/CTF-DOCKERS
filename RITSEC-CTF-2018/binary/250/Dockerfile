FROM ubuntu:16.04

RUN useradd -s /bin/bash -m -d /home/pwn2user pwn2user
WORKDIR /home/pwn2user

RUN apt-get update && \
    apt-get -y install socat libc6-dev-i386

ADD ./dist/pwn2 /home/pwn2user/pwn2
RUN chown pwn2user:pwn2user /home/pwn2user/pwn2
RUN chmod +x /home/pwn2user/pwn2

ADD flag.txt /home/pwn2user/flag.txt
RUN chown pwn2user:pwn2user /home/pwn2user/flag.txt

USER pwn2user

CMD socat TCP-LISTEN:1337,reuseaddr,fork EXEC:"/home/pwn2user/pwn2"