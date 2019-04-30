#!/usr/bin/env python3
import click
import time as watch
from bda_core.use_cases.log.log_info import log_info
from bda_core.use_cases.nlp.normalize_doc import normalize_doc_stream


@click.command()
def normalize():
    start = watch.time()
    doc = click.get_text_stream('stdin', 'utf-8').readlines()

    log_info(f'normalizing')

    for i, line in enumerate(normalize_doc_stream(doc)):
        click.get_text_stream('stdout', 'utf-8').write(f'{line}\n')

    log_info(f'normalized {i+1} lines')
    log_info(f'normalization completed in {watch.time() - start}s\n')


if __name__ == '__main__':
    normalize()
