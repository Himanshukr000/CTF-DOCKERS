FROM richarvey/nginx-php-fpm
COPY files/ /var/www/html
#COPY start.sh /start.sh
COPY default.conf /etc/nginx/sites-enabled/default.conf
#RUN apk add mariadb mariadb-client
#RUN mysql_install_db --user=mysql --datadir=/var/lib/mysql
