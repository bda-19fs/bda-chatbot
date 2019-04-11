#!/usr/bin/env python3
import click
import time as watch
from os import sys, path

# add modules from parent to path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from use_cases.log.log_info import log_info
from use_cases.nlp.remove_stopwords import remove_stopwords_stream


@click.command()
@click.option(
    '-s', '--stopwords', type=click.STRING, default='res/custom_ch_stopwords.txt',
    help='stopwords file in pipeline (default is "res/custom_ch_stopwords.txt")'
)
def stopwords(stopwords):
    start = watch.time()
    doc = click.get_text_stream('stdin', 'utf-8').read()

    log_info(f'remove stopwords')

    lines = remove_stopwords_stream(doc, stopwords)

    log_info(f'removed stopwords from {lines} lines')
    log_info(f'removal of stopwords completed in {watch.time() - start}s\n')


if __name__ == '__main__':
    stopwords()
