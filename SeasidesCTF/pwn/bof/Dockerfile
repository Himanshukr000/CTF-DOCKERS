FROM ubuntu:latest
#installation
RUN dpkg --add-architecture i386
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y socat build-essential libc6:i386 libncurses5:i386 libstdc++6:i386

#add user
RUN adduser --disabled-password --gecos '' classico

#securityRestrictions
RUN chown -R root:classico /home/classico/
RUN chmod 750 /home/classico
RUN chmod 740 /usr/bin/top
RUN chmod 740 /bin/ps
RUN chmod 740 /usr/bin/pgrep
RUN export TERM=xterm

WORKDIR /home/classico/

COPY classico /home/classico
COPY flag /home/classico

RUN chown root:classico /home/classico/flag
RUN chmod 440 /home/classico/flag

EXPOSE 10004
CMD su classico -c "socat -T10 TCP-LISTEN:10004,reuseaddr,fork EXEC:/home/classico/classico"
