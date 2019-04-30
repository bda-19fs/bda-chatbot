#!/usr/bin/env python3
import click
import time as watch
from bda_core.use_cases.log.log_info import log_info
from bda_core.use_cases.nlp.stemm_doc import stemm_doc_stream


@click.command()
@click.option(
    '-l', '--language', type=click.STRING, default='de',
    help='choose vocabular language (default is "de")'
)
def stemm(language):
    start = watch.time()
    doc = click.get_text_stream('stdin', 'utf-8').readlines()

    log_info(f'stemming')

    for i, line in enumerate(stemm_doc_stream(doc, language)):
        click.get_text_stream('stdout', 'utf-8').write(f'{line}\n')

    log_info(f'stemmed {i+1} lines')
    log_info(f'stemming completed in {watch.time() - start}s\n')


if __name__ == '__main__':
    stemm()
