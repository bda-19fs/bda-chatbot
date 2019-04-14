FROM python:3.7-alpine

RUN apk add --no-cache bash
RUN mkdir /usr/src/app
WORKDIR /usr/src/app

COPY ./wiki_extract .
COPY ./core ./core