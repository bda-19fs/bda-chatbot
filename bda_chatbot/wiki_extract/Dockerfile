FROM python:3.7-alpine

RUN apk add --no-cache bash
RUN mkdir /app
RUN mkdir /app/wiki_dumps

ADD ./wiki_extract /app
ADD ./app /app

RUN pip install -r /app/requirements.txt
