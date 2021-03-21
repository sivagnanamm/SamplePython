FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get clean
RUN apt-get update -y --fix-missing
RUN apt-get install -y python3-pip python3-dev build-essential
RUN pip3 install --upgrade pip
ENV LC_ALL=C.UTF-8

COPY Service3 /service3
WORKDIR /service3

RUN pip3 install -r requirements.txt

ENTRYPOINT ["uwsgi --ini conf.ini"]

