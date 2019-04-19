import click
from bda_core.entities.file.json_handler import from_str_to_json, dump_json


def extract_json_documents(doc):
    doc = list(filter(lambda x: x != '', doc.split('\n')))
    json_data = [extract_json_document(line) for line in doc]
    return json_data


def extract_json_document(doc):
    return from_str_to_json(doc)


def write_articles_out(json_docs):
    for doc in json_docs:
        write_article_out(doc)


def write_article_out(json_doc):
    click.get_text_stream('stdout', 'utf-8').write(dump_json(json_doc) + '\n')
