FROM ubuntu:16.04
#installation
RUN dpkg --add-architecture i386
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y socat build-essential libc6:i386 libncurses5:i386 libstdc++6:i386

#add user
RUN adduser --disabled-password --gecos '' raceme

#securityRestrictions
RUN chown -R root:raceme /home/raceme/
RUN chmod 750 /home/raceme
RUN chmod 740 /usr/bin/top
RUN chmod 740 /bin/ps
RUN chmod 740 /usr/bin/pgrep
RUN export TERM=xterm

WORKDIR /home/raceme/

COPY raceme /home/raceme
COPY flag /home/raceme

RUN chown root:raceme /home/raceme/flag
RUN chmod 440 /home/raceme/flag

EXPOSE 31336
CMD su raceme -c "socat -T10 TCP-LISTEN:31336,reuseaddr,fork EXEC:/home/raceme/raceme"
