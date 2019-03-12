# Basic Xinetd Docker Container

FROM debian
MAINTAINER ctf@unswsecurity.com
ENTRYPOINT ["/home/ctf/challenge"]


RUN apt-get update && apt-get -y install python python-dev python-flask python-flask-login python-flaskext.wtf python-flask-sqlalchemy python-twisted python-wtforms python-pip libffi-dev libssl-dev fontconfig curl
RUN pip install --upgrade cffi
RUN pip install selenium flask-user

# Add the ctf user
RUN mkdir /home/ctf
RUN chmod 755 /home/ctf

RUN useradd -M -U\
    -d /home/ctf \
    ctf

RUN chown ctf:ctf /home/ctf

# Add the content
ADD content/* /home/ctf/

RUN /home/ctf/installphantom
RUN chown -R ctf: /home/ctf/

# Expose the service port
EXPOSE 9091
