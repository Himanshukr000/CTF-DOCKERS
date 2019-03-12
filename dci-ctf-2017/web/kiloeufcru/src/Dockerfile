FROM ubuntu:16.04

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y apache2 php7.0 libapache2-mod-php7.0 php7.0-sqlite

RUN a2enmod rewrite

RUN ln -sf /dev/stdout /var/log/apache2/error.log

COPY ./html /var/www/html
COPY ./data.db /var/www
RUN rm /var/www/html/index.html
RUN mv /var/www/html/.mygit /var/www/html/.git

RUN sed -i '/<Directory \/var\/www\/>/,/<\/Directory>/ s/AllowOverride None/AllowOverride All/' /etc/apache2/apache2.conf

CMD /usr/sbin/apache2ctl -D FOREGROUND