#!/bin/sh


python3 /app/wiki_extractor.py /mnt/data/raw/xml/enwiki-latest-pages-articles.xml -o data --json --filter_by_ids -ac /wiki_extract/en_article_ids_stackexchange.csv
mv -vf /wiki_extract/data/AA/* /mnt/data/raw/wiki/en
rm -rf /wiki_extract/data

python3 /app/wiki_extractor.py /mnt/data/raw/xml/dewiki-21032019-pages-articles.xml -o data --json --filter_by_ids -ac /wiki_extract/de_article_ids_ionesoft.csv
mv -vf /wiki_extract/data/AA/* /mnt/data/raw/wiki/de
rm -rf /wiki_extract/data
