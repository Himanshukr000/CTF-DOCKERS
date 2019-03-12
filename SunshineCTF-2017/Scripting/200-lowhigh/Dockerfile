FROM ubuntu

# Install updates
RUN apt-get update && \
	apt-get upgrade -y

# Install python and socat
RUN apt-get install -y python socat

# Create challenge directory
WORKDIR /challenge

# Copy challenge files
COPY run.sh server.py flag.txt ./

# run.sh will start a socat server
EXPOSE 30002
CMD ["./run.sh"]
