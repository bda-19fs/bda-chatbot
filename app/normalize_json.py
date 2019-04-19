#!/usr/bin/env python3
import click
import time as watch
from bda_core.use_cases.log.log_info import log_info
from bda_core.use_cases.nlp.normalize_doc import normalize_json_stream
from bda_core.use_cases.wiki.extract_article import extract_json_documents


@click.command()
def normalize():
    start = watch.time()
    doc = click.get_text_stream('stdin', 'utf-8').read()

    log_info(f'normalizing json')

    doc = extract_json_documents(doc)
    normalize_json_stream(doc)

    log_info(f'normalization completed in {watch.time() - start}s\n')


if __name__ == '__main__':
    normalize()
