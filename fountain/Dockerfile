FROM fserena/python-base:latest
MAINTAINER <fserena@fi.upm.es>

WORKDIR /root

RUN .env/bin/pip install git+https://github.com/oeg-upm/agora-py.git
ADD fountain.py fountain.py

# Configure runit
ADD ./my_init.d/ /etc/my_init.d/
RUN find /etc/my_init.d/ -type f -iname "*.sh" -exec chmod +x {} \;

ONBUILD ADD ./my_init.d/ /etc/my_init.d/

CMD ["/sbin/my_init"]

EXPOSE 5000
