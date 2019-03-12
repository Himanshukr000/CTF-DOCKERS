# Base
FROM centos:latest

# Prep
RUN yum -y install nc net-tools nmap file tcpdump unzip
RUN adduser -u 1000 -g 10 centos
RUN adduser -u 1010 -g 10 web
WORKDIR /home/centos

# 01
RUN mkdir flag_dir && touch flag_dir/FLAG1_31337

# 02
RUN mkdir -p .hidden_flag_dir/abc/123/.nothingtoseehere/data && echo FLAG2_42448 > .hidden_flag_dir/abc/123/.nothingtoseehere/data/flag

# 03
RUN cat /dev/random | head -100 > /tmp/.flag3 && echo 'FLAG3_55352' >> /tmp/.flag3 && cat /dev/random | head -100 >> /tmp/.flag3

# 04
RUN echo FLAG4_63992 | base64 > /tmp/.flag4

# 05 - NOOP - see CMD

# 06
RUN adduser -u 1001 -g 10 www && sed -i '/^wheel:/ s/$/www,FLAG6_41442/' /etc/group

# 07
RUN echo FLAG7_55241 > /home/www/file && chown www /home/www/file && chmod 660 /home/www/file && chmod a+rx /home/www && chgrp wheel /home/www/file && touch /home/www/private && chmod 600 /home/www/private

# 08 - NOOP

# 09 - see CMD
COPY flag_http /tmp/.flag_http

# 10 - NOOP - see CMD

# 11 - NOOP - Python script

# 12
ADD oddfile.zip oddfile.zip

# 14
ADD flag.dmp flag.dmp

# User
USER centos

# Command
CMD nc -lkp 31337 -c 'echo FLAG_11314' & nc -lkp 8080 -c 'cat /tmp/.flag_http' & bash

# Ports
EXPOSE 31337 8080
