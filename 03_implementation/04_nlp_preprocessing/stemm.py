#!/usr/bin/env python
import click
import time as watch
from lib.log_handler import log_info
from lib.nlp_methods import stemming_iterator


@click.command()
def stemm():
    start = watch.time()
    doc = click.get_text_stream('stdin', 'utf-8').read()

    log_info(f'stemming')

    lines = 0
    for line in stemming_iterator(doc):
        if line is None:
            break
        click.get_text_stream('stdout', 'utf-8').write(line + '\n')
        lines += 1

    log_info(f'stemmed {lines} lines')
    log_info(f'stemming completed in {watch.time() - start}s\n')


if __name__ == '__main__':
    stemm()
