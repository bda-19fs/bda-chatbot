#!/usr/bin/env python3
import click
from bda_core.entities.file.reader import (
    file_as_dict,
    file_as_list
)


@click.command()
@click.option(
    '-m', '--map', type=click.STRING, required=True,
    help='choose file containing category to answer'
)
@click.option(
    '-f', '--file', type=click.STRING, required=True,
    help='choose file containing categories'
)
def category_to_answer(map, file):
    map = file_as_dict(map, sep=';', local=False)
    map =  {k.lower(): v for k, v in map.items()}
    cat = file_as_list(file, local=False)

    for c in cat:
        if c not in map:
            print(c)


if __name__ == '__main__':
    category_to_answer()
