FROM python:3.7-alpine

ADD ./backend /usr/src/app
ADD ./app/bda_core /usr/src/app/bda_core
WORKDIR /usr/src/app

RUN pip install -r requirements.txt

ENV FLASK_ENV development
ENV FLASK_APP api.py

EXPOSE 5000
CMD ["flask", "run", "-h", "0.0.0.0"]
