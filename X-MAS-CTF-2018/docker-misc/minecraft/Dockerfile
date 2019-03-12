FROM java:9
COPY files/ /chall
RUN adduser --disabled-password --gecos '' friend
RUN chmod 777 /chall
RUN chmod 555 /chall/*
WORKDIR /chall
RUN chmod 755 world
RUN chmod 755 server.properties
RUN chown -R friend world
RUN chown friend server.properties
USER friend
CMD ["python", "host.py"]
