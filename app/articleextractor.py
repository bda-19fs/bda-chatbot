#!/usr/bin/env python3
import click
import time as watch
from os import sys, path

# add modules from parent to path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from bda_core.use_cases.log.log_info import log_info
from bda_core.use_cases.file.extract_json import extract_json_documents, write_article_out

from bda_core.use_cases.nlp.normalize_doc import normalize_json
from bda_core.use_cases.nlp.remove_stopwords import remove_stopwords_json
from bda_core.use_cases.nlp.stemm_doc import stemm_json


@click.command()
@click.option(
    '-l', '--language', type=click.STRING, default='de',
    help='choose vocabular language (default is "de")'
)
def extract(language):
    start = watch.time()
    doc = click.get_text_stream('stdin', 'utf-8').read()

    log_info(f'extract articles from raw data')

    json_docs = extract_json_documents(doc)
    #norm_json_docs = [article_pipeline(j, language) for j in json_docs]
    #write_articles_out(norm_json_docs)

    for doc in json_docs:
        write_article_out(doc)

    log_info(f'article extracting ended in {watch.time() - start}s\n')


def article_pipeline(json_doc, language):
    text_key = 'text'
    json_doc = normalize_json(json_doc, text_key)
    json_doc = remove_stopwords_json(json_doc, text_key)
    json_doc = stemm_json(json_doc, text_key, language)
    return json_doc


if __name__ == '__main__':
    extract()
