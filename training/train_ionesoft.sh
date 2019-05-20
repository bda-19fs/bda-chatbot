#!/bin/sh

python3 /app/training.py -w /mnt/data/raw/wiki/de/ -q /mnt/data/raw/ionesoft_questions.txt normalize grammar
python3 /app/training.py -w /mnt/data/raw/wiki/de/ -q /mnt/data/raw/ionesoft_questions.txt -n "stemming_" normalize grammar stemm
python3 /app/training.py -w /mnt/data/raw/wiki/de/ -q /mnt/data/raw/ionesoft_questions.txt -n "lemming_" normalize grammar lemm
python3 /app/training.py -w /mnt/data/raw/wiki/de/ -q /mnt/data/raw/ionesoft_questions.txt -n "stopwords_" normalize grammar stopwords
python3 /app/training.py -w /mnt/data/raw/wiki/de/ -q /mnt/data/raw/ionesoft_questions.txt -n "stopwords_stemming_" normalize grammar stopwords stemm
python3 /app/training.py -w /mnt/data/raw/wiki/de/ -q /mnt/data/raw/ionesoft_questions.txt -n "stopwords_lemming_" normalize grammar stopwords lemm

python3 /app/training_w2v.py -w /mnt/data/raw/wiki/de/ -q /mnt/data/raw/ionesoft_questions.txt normalize grammar
python3 /app/training_w2v.py -w /mnt/data/raw/wiki/de/ -q /mnt/data/raw/ionesoft_questions.txt -n "stemming_" normalize grammar stemm
python3 /app/training_w2v.py -w /mnt/data/raw/wiki/de/ -q /mnt/data/raw/ionesoft_questions.txt -n "lemming_" normalize grammar lemm
python3 /app/training_w2v.py -w /mnt/data/raw/wiki/de/ -q /mnt/data/raw/ionesoft_questions.txt -n "stopwords_" normalize grammar stopwords
python3 /app/training_w2v.py -w /mnt/data/raw/wiki/de/ -q /mnt/data/raw/ionesoft_questions.txt -n "stopwords_stemming_" normalize grammar stopwords stemm
python3 /app/training_w2v.py -w /mnt/data/raw/wiki/de/ -q /mnt/data/raw/ionesoft_questions.txt -n "stopwords_lemming_" normalize grammar stopwords lemm
