#!/bin/sh
echo "Starting fountain container..."

/root/.env/bin/pip install --upgrade redislite
/root/.env/bin/pip install --upgrade git+https://github.com/fserena/agora-py.git
/root/.env/bin/python fountain.py &
