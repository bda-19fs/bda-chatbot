#!/usr/bin/env python
import click
import time as watch
from lib.csv_handler import csv_iterator
from lib.log_handler import log_info


@click.command()
@click.option(
    '-c', '--column', type=click.INT, required=True,
    help='column number to export (starting at 0)'
)
@click.option(
    '-s', '--seperator', type=click.STRING, default=',',
    help='column separator (default is ",")'
)
def extract(column, seperator):
    start = watch.time()
    csv = click.get_text_stream('stdin').read()

    log_info(f'extracting column: {column} seperator: {seperator}')

    lines = 0
    for value in csv_iterator(csv, column, seperator):
        click.get_text_stream('stdout').write(value + '\n')
        lines += 1

    log_info(f'extracted {lines} lines')
    log_info(f'extraction completed in {watch.time() - start}s\n')


if __name__ == '__main__':
    extract()
