#!/usr/bin/env bash

export FLASK_APP=./src/app.py
source $(pipenv --venv)/bin/activate
uwsgi --socket 0.0.0.0:5000 --protocol=http --ini random_api.ini --wsgi-file wsgi.py