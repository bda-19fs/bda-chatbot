# Extract the necessary articles from the wiki dump
python3 ./WikiExtractor.py data/de_small_dump.xml -o data --json --filter_by_ids -ac de_article_ids_ionesoft.csv

cat data/de_small_articles.raw | python3 ./articleextractor.py