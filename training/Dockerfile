FROM python:3.7.3


ADD ./training /training
ADD ./app /app

WORKDIR /training

RUN pip3 install -r requirements.txt
RUN chmod +x train_stackexchange.sh
RUN chmod +x train_ionesoft.sh
RUN chmod +x nltk_download.sh

CMD ["/training/nltk_download.sh"]

WORKDIR /mnt/data/models/stackexchange
CMD ["/training/train_stackexchange.sh"]

WORKDIR /mnt/data/models/ionesoft
CMD ["/training/train_ionesoft.sh"]
