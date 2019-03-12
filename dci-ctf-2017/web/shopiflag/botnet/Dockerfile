FROM php:7.0-apache

RUN docker-php-ext-install pdo pdo_mysql

COPY php.ini /usr/local/etc/php/
COPY public/ /var/www/html/

RUN chown -R root:www-data /var/www
RUN chmod 1775 -R /var/www/
RUN chmod 440 /var/www/html/secret/flag.txt