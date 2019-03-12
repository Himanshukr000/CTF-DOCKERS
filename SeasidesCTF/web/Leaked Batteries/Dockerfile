FROM python:3.6.7

COPY ./requirements.txt /deploy/app/

WORKDIR /deploy/app

RUN chmod 444 /deploy/app/*.txt

RUN pip3 install -r /deploy/app/requirements.txt
RUN pip3 install gunicorn

# Start gunicorn
CMD ["gunicorn","-w", "4", "-b", "0.0.0.0:8000", "application:app"]
