#!/usr/bin/env python3
import click
import time as watch
from lib.log_handler import log_info
from lib.nlp_normalize import nlp_normalize


@click.command()
def normalize():
    start = watch.time()
    doc = click.get_text_stream('stdin', 'utf-8').read()

    log_info(f'normalizing')

    lines = nlp_normalize(doc)

    log_info(f'normalized {lines} lines')
    log_info(f'normalization completed in {watch.time() - start}s\n')


if __name__ == '__main__':
    normalize()
