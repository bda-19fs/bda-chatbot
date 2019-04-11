#!/usr/bin/env python3
import click
import time as watch
from os import sys, path

# add modules from parent to path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from use_cases.log.log_info import log_info
from use_cases.nlp.normalize_doc import normalize_doc_stream


@click.command()
def normalize():
    start = watch.time()
    doc = click.get_text_stream('stdin', 'utf-8').read()

    log_info(f'normalizing')

    lines = normalize_doc_stream(doc)

    log_info(f'normalized {lines} lines')
    log_info(f'normalization completed in {watch.time() - start}s\n')


if __name__ == '__main__':
    normalize()
