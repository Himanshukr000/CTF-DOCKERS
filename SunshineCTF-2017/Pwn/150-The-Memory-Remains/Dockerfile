#Import the pwnableharness docker image from https://hub.docker.com/r/c0deh4cker/pwnableharness/
FROM c0deh4cker/pwnableharness

#Copy over the flag.txt file
COPY flag.txt ./

#Set permissions for the flag.txt file
RUN chown root:$RUNTIME_NAME flag.txt && \
	chmod 0640 flag.txt

#Define the port which the docker container will be accessible over
EXPOSE 20002 
