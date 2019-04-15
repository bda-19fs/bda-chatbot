#!/usr/bin/env python3
import click
import time as watch
from os import sys, path

# add modules from parent to path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from use_cases.log.log_info import log_info
from use_cases.wiki.extract_article import extract_json_documents

from use_cases.nlp.normalize_doc import normalize_doc
from use_cases.nlp.remove_stopwords import remove_stopwords

@click.command()
def extract():
    start = watch.time()
    doc = click.get_text_stream('stdin', 'utf-8').read()

    log_info(f'extract articles from raw data')
    json_docs = extract_json_documents(doc)
    norm_json_docs = [article_pipeline(j) for j in json_docs]
    write_normalized_articles(norm_json_docs)

    log_info(f'correction completed in {watch.time() - start}s\n')


def article_pipeline(json_doc):
    article_text = json_doc['text']

    article_text = normalize_doc(article_text)
    article_text = remove_stopwords(article_text)

    json_doc['text'] = article_text
    return json_doc


def write_normalized_articles(json_docs):
    for doc in json_docs:
        click.get_text_stream('stdout', 'utf-8').write(doc + '\n')


if __name__ == '__main__':
    extract()
