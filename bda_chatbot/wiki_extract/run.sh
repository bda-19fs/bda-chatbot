# Extract the necessary articles from the wiki dump
python3 use_cases/wiki/WikiExtractor.py /wiki_dumps/de_small_dump.xml --filter_by_ids -ac ./de_article_ids_ionesoft.csv --json
