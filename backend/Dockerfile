FROM python:3.7.2

ADD ./backend /usr/src/app
ADD ./app/bda_core /usr/src/app/bda_core
WORKDIR /usr/src/app

RUN pip3 install -r requirements.txt

ENV FLASK_ENV development
ENV FLASK_APP api.py

EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "-t", "60000", "api:app"]
