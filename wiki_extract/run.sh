# Extract the necessary articles from the wiki dump
python3 ./WikiExtractor.py wiki_dumps/de_small_dump.xml -o wiki_dumps --json --filter_by_ids -ac de_article_ids_ionesoft.csv

cat wiki_dumps/de_small_articles.raw | python3 ./articleextractor.py