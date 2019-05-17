FROM python:3.7.3


ADD ./training /training
ADD ./app /app

WORKDIR /training

RUN pip3 install -r requirements.txt
RUN chmod +x train.sh

WORKDIR /mnt/data/models

CMD ["sleep", "60000"]

