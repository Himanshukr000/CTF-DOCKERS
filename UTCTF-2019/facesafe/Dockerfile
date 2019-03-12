FROM python:2

ARG APP_PATH=/locker

#RUN apk --update add python py-pip python-dev build-base linux-headers
#RUN apk --update add  openssl python3 python-dev build-base linux-headers
#RUN update-ca-certificates

#RUN wget -O /tmp/models.tar.gz https://drive.google.com/file/d/1SqLHneiEXNSbZCqaINyMSuJ8E0fkSe3t/view?usp=sharing
RUN mkdir -p $APP_PATH/locker
#RUN tar -zcvf /tmp/models.tar.gz -C $APP_PATH/locker/models
#RUN rm /tmp/models.tar.gz

#ENV LOAD_MODELS=false
ENV PYTHONUNBUFFERED 1

#RUN apk --update add python py-pip python-dev build-base linux-headers py-gevent
# py-gevent
COPY requirements.txt $APP_PATH/requirements.txt
#COPY requirements-web.txt $APP_PATH/requirements-web.txt
RUN pip install -r $APP_PATH/requirements.txt
#RUN pip install -r $APP_PATH/requirements-web.txt
#RUN CFLAGS="$CFLAGS -L/lib" pip install uwsgi
#RUN pip install uwsgi

COPY . $APP_PATH

WORKDIR $APP_PATH

ENTRYPOINT [ "python" ]

CMD [ "runserver.py" ]

#CMD ["uwsgi", "--static-map", "/static=locker/static", "--http", ":8000", "--module", "locker:app"]

