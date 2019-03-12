FROM php:7.0-apache

RUN docker-php-ext-install pdo pdo_mysql

RUN a2enmod rewrite
RUN service apache2 restart

COPY php.ini /usr/local/etc/php/
COPY public/ /var/www/html/