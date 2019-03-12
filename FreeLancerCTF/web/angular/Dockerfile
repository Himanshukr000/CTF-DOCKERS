# Basic Xinetd Docker Container

FROM debian
MAINTAINER ctf@unswsecurity.com
ENTRYPOINT ["/home/ctf/challenge"]

RUN apt-get update && apt-get -y install python python-dev libffi-dev libssl-dev fontconfig python-setuptools python-pip
RUN dpkg -r python-pip && easy_install pip
RUN apt-get -y install python-twisted python-cffi python-crypto

# Add the ctf user
RUN mkdir /home/ctf
RUN chmod 755 /home/ctf

RUN useradd -M -U\
    -d /home/ctf \
    ctf

RUN chown ctf:ctf /home/ctf

# Add the content
#ADD ./content /home/ctf/
ADD content /home/ctf/

RUN chown -R ctf: /home/ctf/
RUN pip install -r /home/ctf/requirements.txt
RUN pip install --upgrade cryptography
#RUN pip install --upgrade cffi

# Expose the service port
EXPOSE 9091
