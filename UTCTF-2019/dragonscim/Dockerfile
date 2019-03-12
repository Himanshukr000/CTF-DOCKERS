FROM php:7.2-apache
MAINTAINER William Han <copperstick6@gmail.com>

RUN a2enmod rewrite

# Expose apache.
EXPOSE 80

# Copy this repo into place.
ADD . /var/www/site

# Update the default apache site with the config we created.
COPY apache-config.conf /etc/apache2/sites-enabled/000-default.conf

# By default start up apache in the foreground, override with /bin/bash for interative.
CMD /usr/sbin/apache2ctl -D FOREGROUND
