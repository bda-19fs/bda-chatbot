#!/bin/sh

python3 /app/training.py -w /mnt/data/raw/wiki/en/ -q /mnt/data/raw/stackexchange_questions.txt normalize
python3 /app/training.py -w /mnt/data/raw/wiki/en/ -q /mnt/data/raw/stackexchange_questions.txt -n "stemming_" normalize stemming -l "en"
python3 /app/training.py -w /mnt/data/raw/wiki/en/ -q /mnt/data/raw/stackexchange_questions.txt -n "lemming_" normalize lemming -l "en"
