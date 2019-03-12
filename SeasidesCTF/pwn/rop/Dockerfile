FROM ubuntu:16.04
#installation
RUN dpkg --add-architecture i386
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y socat build-essential libc6:i386 libncurses5:i386 libstdc++6:i386

#add user
RUN adduser --disabled-password --gecos '' modern

#securityRestrictions
RUN chown -R root:modern /home/modern/
RUN chmod 750 /home/modern
RUN chmod 740 /usr/bin/top
RUN chmod 740 /bin/ps
RUN chmod 740 /usr/bin/pgrep
RUN export TERM=xterm

WORKDIR /home/modern/

COPY modern /home/modern
COPY flag /home/modern

RUN chown root:modern /home/modern/flag
RUN chmod 440 /home/modern/flag

EXPOSE 10002
CMD su modern -c "socat -T10 TCP-LISTEN:10002,reuseaddr,fork EXEC:/home/modern/modern"
