FROM ubuntu:latest
#installation
RUN dpkg --add-architecture i386
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y socat build-essential libc6:i386 libncurses5:i386 libstdc++6:i386

#add user
RUN adduser --disabled-password --gecos '' allocator

#securityRestrictions
RUN chown -R root:allocator /home/allocator/
RUN chmod 750 /home/allocator
RUN chmod 740 /usr/bin/top
RUN chmod 740 /bin/ps
RUN chmod 740 /usr/bin/pgrep
RUN export TERM=xterm

WORKDIR /home/allocator/

COPY allocator /home/allocator
COPY flag /home/allocator

RUN chown root:allocator /home/allocator/flag
RUN chmod 440 /home/allocator/flag

EXPOSE 10005
CMD su allocator -c "socat -T10 TCP-LISTEN:10005,reuseaddr,fork EXEC:/home/allocator/allocator"
