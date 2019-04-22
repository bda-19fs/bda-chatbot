FROM python:3.7-alpine

RUN apk add --no-cache bash
WORKDIR /app
ADD ./app .
ADD ./training .

RUN pip install -r /app/requirements.txt
