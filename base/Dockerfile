FROM phusion/baseimage:latest
MAINTAINER <fserena@fi.upm.es>

RUN apt-get update
RUN apt-get install -y build-essential python-dev python-virtualenv python git

WORKDIR /root

RUN virtualenv .env
RUN .env/bin/pip install -U pip

# Configure runit
ADD ./my_init.d/ /etc/my_init.d/

ONBUILD ADD ./my_init.d/ /etc/my_init.d/


CMD ["/sbin/my_init"]

EXPOSE 5000
