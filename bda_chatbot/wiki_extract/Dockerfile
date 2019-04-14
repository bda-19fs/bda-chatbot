FROM python:3.7-alpine

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

COPY ./wiki_extract .
COPY ./core ./core

RUN ./run.sh