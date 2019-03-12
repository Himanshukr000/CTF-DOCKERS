FROM python:3.6.7-alpine
RUN pip3 install discord
RUN pip3 install requests

COPY files/ /mecha
WORKDIR /mecha
RUN chmod 111 mecha.py
RUN chmod 555 robot_restart_codes.txt
CMD ["python3", "mecha.py"]