FROM richarvey/nginx-php-fpm:latest
COPY default.conf /etc/nginx/sites-enabled/default.conf
COPY files/ /var/www/html
RUN chmod 555 /var/www/html
RUN chmod 555 /etc/nginx/sites-enabled/default.conf
RUN chmod 555 /etc/nginx/nginx.conf
RUN chmod 555 flag.txt
RUN chmod 555 index.php
RUN chmod 555 500.html
RUN chmod 1755 uploads
RUN chmod 1755 img
RUN chmod 555 img/BG.png
RUN chmod 555 img/vault.png
COPY start.sh /start.sh
RUN chmod +x /start.sh
RUN echo "root:10dcpasdom210cposcPCD" | chpasswd
