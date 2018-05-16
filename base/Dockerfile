FROM phusion/baseimage:latest
LABEL author="Fernando Serena"

RUN apt-get update
RUN apt-get install -y build-essential python-dev python-virtualenv python git

WORKDIR /root

RUN virtualenv .env
RUN .env/bin/pip install --upgrade pip

# Configure runit
ADD ./my_init.d/ /etc/my_init.d/

ONBUILD ADD ./my_init.d/ /etc/my_init.d/


CMD ["/sbin/my_init"]

