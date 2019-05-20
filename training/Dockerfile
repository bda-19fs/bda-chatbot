FROM python:3.7.3


ADD ./training /training
ADD ./app /app

WORKDIR /training

RUN pip3 install -r requirements.txt
RUN chmod +x train_stackexchange.sh
RUN chmod +x train_ionesoft.sh
RUN chmod +x nltk_download.sh

RUN /training/nltk_download.sh

CMD cd /mnt/data/models/stackexchange && /training/train_stackexchange.sh && cd /mnt/data/models/ionesoft && /training/train_ionesoft.sh
