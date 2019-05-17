#!/bin/sh

python3 /app/training.py -w /mnt/data/raw/wiki/de/ -q /mnt/data/raw/ionesoft_questions.txt normalize
python3 /app/training.py -w /mnt/data/raw/wiki/de/ -q /mnt/data/raw/ionesoft_questions.txt -n "stemming" normalize stemming
python3 /app/training.py -w /mnt/data/raw/wiki/de/ -q /mnt/data/raw/ionesoft_questions.txt -n "lemming" normalize lemming

