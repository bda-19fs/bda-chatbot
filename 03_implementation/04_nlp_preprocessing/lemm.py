#!/usr/bin/env python3
import click
import time as watch
from lib.log_handler import log_info
from lib.nlp_lemming import nlp_lemming


@click.command()
@click.option(
    '-v', '--vocabular', type=click.STRING, default="res/custom_ch_vocabular.txt",
    help='use vocabular file to lemm words (default is "res/custom_ch_vocabular.txt")'
)
def lemm(vocabular):
    start = watch.time()
    doc = click.get_text_stream('stdin', 'utf-8').read()

    log_info(f'stemming')

    lines = nlp_lemming(doc, vocabular)

    log_info(f'stemmed {lines} lines')
    log_info(f'stemming completed in {watch.time() - start}s\n')


if __name__ == '__main__':
    lemm()
