FROM ubuntu
MAINTAINER C0deH4cker <c0deh4cker@gmail.com>

# Install updates
RUN apt-get update && \
	apt-get upgrade -y

# Install python, socat, and sudo
RUN apt-get install -y python socat sudo

# Create unprivileged notetorious user
RUN groupadd -r notetorious && \
	useradd -r -g notetorious notetorious

# Create semi-privileged notetorious_auth user
RUN groupadd -r notetorious_auth && \
	useradd -r -g notetorious_auth -G notetorious notetorious_auth
COPY notetorious_auth.sudoers /etc/sudoers.d/notetorious_auth

# Make directory structure
WORKDIR /notetorious/data/vputin

# Copy files to target locations
COPY start.sh login.py notetorious.py /notetorious/
COPY flag.txt /notetorious/data/vputin/nuclear_launch_codes
COPY russian_flag.txt /notetorious/data/vputin/flag

# Randomly generate vputin's password file
RUN dd if=/dev/urandom of=/notetorious/data/vputin.password bs=1 count=64

# Set ownership and permissions
RUN chown root:notetorious_auth /notetorious/data && \
	chmod 0775 /notetorious/data && \
	chown root:notetorious /notetorious/data/vputin && \
	chmod 0750 /notetorious/data/vputin && \
	chown root:notetorious_auth /notetorious/data/vputin.password && \
	chmod 0640 /notetorious/data/vputin.password && \
	chown root:notetorious /notetorious/data/vputin/flag && \
	chmod 0640 /notetorious/data/vputin/flag

# This challenge listens on the following port
EXPOSE 20003

# Run `start.sh` as root. It will drop privileges for connections
WORKDIR /notetorious
CMD ["/notetorious/start.sh"]
