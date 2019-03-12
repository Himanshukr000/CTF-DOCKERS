FROM ubuntu:16.04
#installation
RUN dpkg --add-architecture i386
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y socat build-essential libc6:i386 libncurses5:i386 libstdc++6:i386

#add user
RUN adduser --disabled-password --gecos '' sho

#securityRestrictions
RUN chown -R root:sho /home/sho/
RUN chmod 750 /home/sho
RUN chmod 740 /usr/bin/top
RUN chmod 740 /bin/ps
RUN chmod 740 /usr/bin/pgrep
RUN export TERM=xterm

WORKDIR /home/sho/

COPY sho /home/sho
COPY flag /home/sho

RUN chown root:sho /home/sho/flag
RUN chmod 440 /home/sho/flag

EXPOSE 10003
CMD su sho -c "socat -T10 TCP-LISTEN:10003,reuseaddr,fork EXEC:/home/sho/sho"
