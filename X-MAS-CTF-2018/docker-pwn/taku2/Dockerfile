#FROM debian:stretch-slim
FROM ubuntu:latest

ENV DEBIAN_FRONTEND noninteractive

#update
RUN apt-get update --fix-missing && apt-get -y upgrade

#system deps
RUN apt-get install -y lib32z1 libseccomp-dev xinetd build-essential linux-headers-generic

#create ctf-user
RUN groupadd -r ctf && useradd -r -g ctf ctf

### IF CHROOT
#RUN cp -R /lib* /home/ctf
#RUN cp -R /usr/lib* /home/ctf
#RUN mkdir /home/ctf/dev
#RUN mknod /home/ctf/dev/null c 1 3
#RUN mknod /home/ctf/dev/zero c 1 5
#RUN mknod /home/ctf/dev/random c 1 8
#RUN mknod /home/ctf/dev/urandom c 1 9
#RUN chmod 666 /home/ctf/dev/*
#RUN mkdir /home/ctf/bin
#RUN cp /bin/sh /home/ctf/bin
#RUN cp /bin/ls /home/ctf/bin
#RUN cp /bin/cat /home/ctf/bin
### IF CHROOT

#add chall items
ADD ctf.xinetd /etc/xinetd.d/ctf
ADD chall_init.sh /etc/chall_init.sh
ADD flag /home/ctf/flag
ADD redir.sh /home/ctf/redir.sh
ADD chall.c /home/ctf/chall.c

RUN gcc /home/ctf/chall.c -o /home/ctf/chall -fno-stack-protector -Wl,-z,relro,-z,now -fPIC -pie
RUN rm /home/ctf/chall.c

#set some proper permissions
RUN chown -R root:ctf /home/ctf
RUN chmod 750 /home/ctf/chall
RUN chmod 750 /home/ctf/redir.sh
RUN chmod 440 /home/ctf/flag
RUN chmod 700 /etc/chall_init.sh

RUN service xinetd restart

### IF NETWORK-DEBUG
#RUN apt-get -y install netcat
#RUN apt-get -y install net-tools
### IF NETWORK-DEBUG
