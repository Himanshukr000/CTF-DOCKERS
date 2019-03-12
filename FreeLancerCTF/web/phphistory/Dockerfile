# A basic webserver to host files

FROM debian
MAINTAINER ctf@unswsecurity.com

# Update repo cache
RUN apt-get update

# Install apache2
RUN apt-get install -y apache2

# Disable autorun of apache
RUN update-rc.d apache2 disable

# Add special dependancies
RUN apt-get install -y php5

# Add data into the web server base
RUN rm -r "/var/www/html/index.php"
ADD ["content.tar.bz2", "/var/www/html/"]

EXPOSE 80
ENTRYPOINT ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
