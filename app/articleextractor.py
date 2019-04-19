#!/usr/bin/env python3
import click
import time as watch
from os import sys, path

# add modules from parent to path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from bda_core.use_cases.log.log_info import log_info
from bda_core.use_cases.file.extract_json import extract_json_documents, write_json_doc_out


@click.command()
def extract():
    start = watch.time()
    doc = click.get_text_stream('stdin', 'utf-8').read()

    log_info(f'extract articles from raw data')

    json_docs = extract_json_documents(doc)

    for doc in json_docs:
        write_json_doc_out(doc)

    log_info(f'article extracting ended in {watch.time() - start}s\n')


if __name__ == '__main__':
    extract()
