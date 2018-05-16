FROM fserena/python-base:latest
LABEL author="Fernando Serena"

WORKDIR /root

RUN .env/bin/pip install git+https://github.com/fserena/agora-py.git
RUN .env/bin/pip install git+https://github.com/fserena/agora-wot.git
RUN .env/bin/pip install git+https://github.com/fserena/agora-gw.git

ADD graph/ graph/
ADD fountain/ fountain/

# Configure runit
ADD ./my_init.d/ /etc/my_init.d/

ONBUILD ADD ./my_init.d/ /etc/my_init.d/

CMD ["/sbin/my_init"]

EXPOSE 8000
