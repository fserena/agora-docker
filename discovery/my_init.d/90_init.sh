#!/bin/sh
echo "Initializing graph repository..."

/root/.env/bin/pip install --upgrade requests

cd graph
/root/.env/bin/python /root/graph/init.py






