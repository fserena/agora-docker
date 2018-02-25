#!/bin/sh
echo "Starting gateway container..."

/root/.env/bin/pip install --upgrade git+https://github.com/oeg-upm/agora-py.git
/root/.env/bin/pip install --upgrade git+https://github.com/oeg-upm/agora-wot.git
/root/.env/bin/pip install --upgrade git+https://github.com/oeg-upm/agora-gw.git

/root/.env/bin/gw &
