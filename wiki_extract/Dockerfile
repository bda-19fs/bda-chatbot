FROM python:3.7.3-alpine


ADD ./wiki_extract /wiki_extract
ADD ./app /app

WORKDIR /wiki_extract

RUN pip3 install -r requirements.txt
RUN chmod +x wiki_extract.sh

CMD ./wiki_extract.sh
