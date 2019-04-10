#!/usr/bin/env python3
import click
import time as watch
from lib.log_handler import log_info
from lib.nlp_stemming import nlp_stemming


@click.command()
def stemm():
    start = watch.time()
    doc = click.get_text_stream('stdin', 'utf-8').read()

    log_info(f'stemming')

    lines = nlp_stemming(doc)
    
    log_info(f'stemmed {lines} lines')
    log_info(f'stemming completed in {watch.time() - start}s\n')


if __name__ == '__main__':
    stemm()
