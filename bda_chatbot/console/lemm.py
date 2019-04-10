#!/usr/bin/env python3
import click
import time as watch
from os import sys, path

# add modules from parent to path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from use_cases.log.log_info import log_info
from use_cases.nlp.lemm_doc import lemm_doc


@click.command()
@click.option(
    '-v', '--vocabular', type=click.STRING, default="res/custom_ch_vocabular.txt",
    help='use vocabular file to lemm words (default is "res/custom_ch_vocabular.txt")'
)
def lemm(vocabular):
    start = watch.time()
    doc = click.get_text_stream('stdin', 'utf-8').read()

    log_info(f'lemming')

    lines = lemm_doc(doc, vocabular)

    log_info(f'lemmed {lines} lines')
    log_info(f'lemming completed in {watch.time() - start}s\n')


if __name__ == '__main__':
    lemm()
