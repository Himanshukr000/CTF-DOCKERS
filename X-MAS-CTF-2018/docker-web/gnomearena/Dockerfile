FROM richarvey/nginx-php-fpm:latest
COPY files/ /var/www/html
COPY default.conf /etc/nginx/sites-enabled/default.conf
RUN chmod 555 /var/www/html
WORKDIR /var/www/html
RUN chmod 555 *
RUN chmod 555 /etc/nginx/sites-enabled/default.conf
RUN chmod 555 /etc/nginx/nginx.conf
RUN chmod 755 avatars
RUN chmod 555 avatars/noimage
COPY start.sh /start.sh
RUN chmod +x /start.sh
RUN echo "root:S9CJSc9012o9pscack210kcda" | chpasswd
EXPOSE 80
