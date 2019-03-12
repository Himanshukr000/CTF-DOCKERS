FROM tutum/apache-php
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y libapache2-mod-php5 php5-mysql
COPY . /app
