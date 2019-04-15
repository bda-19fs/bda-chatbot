#!/usr/bin/env python3
import click
import time as watch
from os import sys, path

# add modules from parent to path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from use_cases.log.log_info import log_info
from use_cases.wiki.extract_article import extract_text_from_article_stream

@click.command()
def extract():
    start = watch.time()
    doc = click.get_text_stream('stdin', 'utf-8').read()

    log_info(f'extract articles from raw data')
    print(doc)
    extract_text_from_article_stream(doc)

    log_info(f'correction completed in {watch.time() - start}s\n')


if __name__ == '__main__':
    extract()
