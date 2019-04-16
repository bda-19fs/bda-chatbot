#!/usr/bin/env python3
import click
import time as watch
from bda_core.use_cases.log.log_info import log_info
from bda_core.use_cases.file.extract_column import extract_column_stream


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

    lines = extract_column_stream(csv, column, separator)

    log_info(f'extracted {lines} lines')
    log_info(f'extraction completed in {watch.time() - start}s\n')


if __name__ == '__main__':
    extract()
