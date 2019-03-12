FROM debian:wheezy
MAINTAINER Emre Bastuz <info@hml.io>

# Environment
ENV LANG C.UTF-8
ENV LANGUAGE C.UTF-8
ENV LC_ALL C.UTF-8

# Get current
RUN apt-get update -y
RUN apt-get dist-upgrade -y

# Install packages
RUN apt-get install -y wget
RUN apt-get install -y apache2

# Install vulnerable bash version from wayback/snapshot archive
RUN wget http://snapshot.debian.org/archive/debian/20130101T091755Z/pool/main/b/bash/bash_4.2%2Bdfsg-0.1_amd64.deb -O /tmp/bash_4.2+dfsg-0.1_amd64.deb && \
 dpkg -i /tmp/bash_4.2+dfsg-0.1_amd64.deb

ENV DEBIAN_FRONTEND noninteractive

# Setup vulnerable web content
ADD index.html /var/www/
ADD stats /usr/lib/cgi-bin/
ADD flag.txt /opt/
RUN chown root:root /opt/flag.txt
RUN chown www-data:www-data /usr/lib/cgi-bin/stats
RUN chmod 644 /opt/flag.txt
RUN chmod u+x /usr/lib/cgi-bin/stats

# Clean up
RUN apt-get autoremove
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Expose the port for usage with the docker -P switch
EXPOSE 80

# Run Apache 2
CMD ["/usr/sbin/apache2ctl", "-DFOREGROUND"]

#
# Dockerfile for vulnerability as a service - CVE-2014-6271
# Vulnerable web application derived from Sokar - a VulnHub machine by rasta_mouse
#
