# Basic Xinetd Docker Container

FROM debian
MAINTAINER ctf@unswsecurity.com
ENTRYPOINT ["/home/ctf/challenge"]


RUN apt-get update && apt-get -y install python python-dev libffi-dev libssl-dev fontconfig python-setuptools python-pip  curl
RUN dpkg -r python-pip && easy_install pip
RUN apt-get -y install python-twisted python-cffi python-crypto
RUN pip install selenium flask-user cffi
RUN pip install --upgrade cryptography


# Add the ctf user
RUN mkdir /home/ctf
RUN chmod 755 /home/ctf

RUN useradd -M -U\
    -d /home/ctf \
    ctf

RUN chown ctf:ctf /home/ctf

# Add the content
ADD ./content /home/ctf/

RUN /home/ctf/installphantom
RUN chown -R ctf: /home/ctf/

# Expose the service port
EXPOSE 9091
