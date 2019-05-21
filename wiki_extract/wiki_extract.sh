#!/bin/sh


python3 /app/wiki_extractor.py /mnt/data/raw/xml/de_small_dump.xml -o data --json --filter_by_ids -ac /wiki_extract/de_article_ids_ionesoft.csv
