FROM python:2.7.14

RUN mkdir -p /usr/src/app

COPY ./src /usr/src/app/src
COPY ./requirements.txt ./wsgi.py ./random-api.ini /usr/src/app/

WORKDIR /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt
