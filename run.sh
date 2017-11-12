#!/usr/bin/env bash

export FLASK_APP=./src/app.py
source ~/anaconda3/bin/activate random-api-env
uwsgi --ini random_api.ini --logto /tmp/uwsgi.log