#
# Extract the necessary articles from the wiki dump
#
python3 WikiExtractor.py /home_static/bda/wiki_dumps/dewiki-21032019-pages-articles.xml --filter_by_ids -ac de_article_ids_ionesoft.csv --json