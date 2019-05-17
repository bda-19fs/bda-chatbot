#!/bin/sh

python3 /app/training.py -w /mnt/data/raw/wiki/en/ -q /mnt/data/raw/stackexchange_questions.txt normalize
python3 /app/training.py -w /mnt/data/raw/wiki/en/ -q /mnt/data/raw/stackexchange_questions.txt -n "stemming_" normalize stemm -l "en"
python3 /app/training.py -w /mnt/data/raw/wiki/en/ -q /mnt/data/raw/stackexchange_questions.txt -n "lemming_" normalize lemm -l "en"
python3 /app/training.py -w /mnt/data/raw/wiki/en/ -q /mnt/data/raw/stackexchange_questions.txt -n "stopwords_" normalize stopwords -s "res/custom_en_stopwords.txt"
python3 /app/training.py -w /mnt/data/raw/wiki/en/ -q /mnt/data/raw/stackexchange_questions.txt -n "stopwords_stemming_" normalize stopwords -s "res/custom_en_stopwords.txt" stemm -l "en"
python3 /app/training.py -w /mnt/data/raw/wiki/en/ -q /mnt/data/raw/stackexchange_questions.txt -n "stopwords_lemming_" normalize stopwords -s "res/custom_en_stopwords.txt" lemm -l "en"
