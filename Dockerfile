FROM python:3.7.4

ENV PYTHONUNBUFFERED 1

RUN apt-get update -y \
    && apt-get install -y \
    libsasl2-dev \
    python-dev \
    libssl-dev \
    python3-dev \
    libpcre3-dev

RUN mkdir -p /usr/app/src
COPY ./src/ /usr/app/src/
COPY ./requirements.txt /usr/app/src
WORKDIR /usr/app/src

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["uwsgi", "--socket", "0.0.0.0:3000", \
              "--protocol", "uwsgi", \
              "--module", "random_api.app", \
              "--callable", "app", \
              "--wsgi-disable-file-wrapper"]