FROM fserena/python-base:latest
MAINTAINER <fserena@fi.upm.es>

WORKDIR /root

RUN .env/bin/pip install git+https://github.com/oeg-upm/agora-py.git
RUN .env/bin/pip install git+https://github.com/oeg-upm/agora-wot.git
RUN .env/bin/pip install git+https://github.com/oeg-upm/agora-gw.git

ADD graph/ graph/
ADD fountain/ fountain/

# Configure runit
ADD ./my_init.d/ /etc/my_init.d/

ONBUILD ADD ./my_init.d/ /etc/my_init.d/

CMD ["/sbin/my_init"]

EXPOSE 8000
