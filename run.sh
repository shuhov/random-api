#!/usr/bin/env bash

export FLASK_APP=./src/app.py
source ~/anaconda3/bin/activate random-api-env
uwsgi --socket 0.0.0.0:5000 --protocol=http --ini random_api.ini --wsgi-file wsgi.py --logto /tmp/uwsgi.log