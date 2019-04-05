#!/usr/bin/env python3
import click
import time as watch
from lib.log_handler import log_info
from lib.extractor import extractor


@click.command()
@click.option(
    '-c', '--column', type=click.INT, required=True,
    help='column number to export (starting at 0)'
)
@click.option(
    '-s', '--separator', type=click.STRING, default=',',
    help='column separator (default is ",")'
)
def extract(column, separator):
    start = watch.time()
    csv = click.get_text_stream('stdin', 'utf-8').read()

    log_info(f'extracting column: {column} separator: {separator}')

    lines = extractor(csv, column, separator)

    log_info(f'extracted {lines} lines')
    log_info(f'extraction completed in {watch.time() - start}s\n')


if __name__ == '__main__':
    extract()
