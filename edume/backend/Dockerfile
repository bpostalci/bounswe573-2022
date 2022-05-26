# syntax=docker/dockerfile:1
FROM ubuntu:20.04
WORKDIR /app
COPY . /app
RUN apt-get update -y
RUN apt-get install libmysqlclient-dev -y
RUN apt-get install python3-pip -y
RUN pip install mysqlclient
RUN pip install -r requirements.txt
CMD . edume/edume.env && \
python3 edume/manage.py makemigrations && \
python3 edume/manage.py migrate && \
python3 edume/manage.py runserver 0.0.0.0:80
