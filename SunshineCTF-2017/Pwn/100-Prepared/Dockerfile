FROM c0deh4cker/pwnableharness
MAINTAINER guyinatuxedo <ryancmeinke@gmail.com>

# Copy the flag to the current directory of the challenge
COPY flag.txt ./

# Make the flag readable only by root or the challenge's group
RUN chown root:$RUNTIME_NAME flag.txt && chmod 0640 flag.txt

# This challenge listens on the following port
EXPOSE 20001
