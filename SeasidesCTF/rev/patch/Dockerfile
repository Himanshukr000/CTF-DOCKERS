FROM ubuntu:latest

RUN dpkg --add-architecture i386
RUN apt-get update && apt-get upgrade -y 
RUN apt-get install -y python3 socat build-essential libc6:i386 libncurses5:i386 libstdc++6:i386

#add user
RUN adduser --disabled-password --gecos '' patch

#securityRestrictions
RUN chown -R root:patch /home/patch/
RUN chmod 750 /home/patch
RUN chmod 740 /usr/bin/top
RUN chmod 740 /bin/ps
RUN chmod 740 /usr/bin/pgrep
RUN export TERM=xterm

WORKDIR /home/patch/

COPY wrapper.py /home/patch
COPY patch /home/patch
COPY flag /home/patch

RUN chown root:patch /home/patch/flag
RUN chmod 440 /home/patch/flag

EXPOSE 10006
CMD su patch -c "socat -T10 TCP-LISTEN:10006,reuseaddr,fork EXEC:/home/patch/wrapper.py"
