FROM python:3.7

COPY server.py ./
COPY hash.py ./
COPY requirements.txt ./

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python","server.py"]
