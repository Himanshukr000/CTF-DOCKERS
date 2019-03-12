FROM php:7.0-apache

RUN a2enmod cgi
RUN a2enmod include

RUN service apache2 restart

COPY flag /flag
COPY getflag /getflag
COPY server-cgi-bin.conf /etc/apache2/conf-enabled/server-cgi-bin.conf
COPY index.html /var/www/html/index.html
COPY ./cgi-bin /usr/lib/cgi-bin/

RUN chmod a+s /getflag
RUN chmod 400 /flag
