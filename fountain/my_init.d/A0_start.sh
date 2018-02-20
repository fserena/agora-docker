#!/bin/sh
echo "Starting fountain container..."

/root/.env/bin/pip install --upgrade git+https://github.com/oeg-upm/agora-py.git
/root/.env/bin/python fountain.py &






