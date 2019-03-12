FROM ubuntu:16.04
#installation
RUN dpkg --add-architecture i386
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y socat build-essential libc6:i386 libncurses5:i386 libstdc++6:i386

#add user
RUN adduser --disabled-password --gecos '' srop

#securityRestrictions
RUN chown -R root:srop /home/srop/
RUN chmod 750 /home/srop
RUN chmod 740 /usr/bin/top
RUN chmod 740 /bin/ps
RUN chmod 740 /usr/bin/pgrep
RUN export TERM=xterm

WORKDIR /home/srop/

COPY srop /home/srop
COPY flag /home/srop

RUN chown root:srop /home/srop/flag
RUN chmod 440 /home/srop/flag

EXPOSE 10001
CMD su srop -c "socat -T10 TCP-LISTEN:10001,reuseaddr,fork EXEC:/home/srop/srop"
