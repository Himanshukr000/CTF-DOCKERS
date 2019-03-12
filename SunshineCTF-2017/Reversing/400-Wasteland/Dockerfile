FROM c0deh4cker/pwnableharness
MAINTAINER guyinatuxedo <ryancmeinke@gmail.com>

# Copy the flag and extra files to the current directory of the challenge
COPY flag.txt 0 1 2 3 4 ./

# Make the flag and extra files readable only by root or the challenge's group
RUN chown root:$RUNTIME_NAME flag.txt 0 1 2 3 4 && \
	chmod 0640 flag.txt 0 1 2 3 4

# This challenge listens on the following port
EXPOSE 10002
