FROM ubuntu:latest
	
RUN apt-get update && apt-get upgrade -y 
RUN apt-get install -y python3 socat build-essential

RUN adduser --disabled-password --gecos '' primes
RUN chown -R root:primes /home/primes/
RUN chmod 770 /home/primes
RUN export TERM=xterm

WORKDIR /home/primes/

COPY primes.py /home/primes
RUN chmod 770 /home/primes/primes.py

EXPOSE 11000
CMD socat -T10 TCP-LISTEN:11000,reuseaddr,fork EXEC:/home/primes/primes.py
