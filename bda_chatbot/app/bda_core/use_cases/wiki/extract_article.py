import click
from bda_core.entities.wiki.json_handler import from_str_to_json, dump_json


def extract_text_from_article_stream(doc):
    doc = list(filter(lambda x: x != '', doc.split('\n')))

    for line in doc:
        json_data = from_str_to_json(line)
        click.get_text_stream('stdout', 'utf-8').write(dump_json(json_data) + '\n')


def extract_json_documents(doc):
    doc = list(filter(lambda x: x != '', doc.split('\n')))
    json_data = [from_str_to_json(line) for line in doc]
    return json_data


def write_articles_out(json_docs):
    for doc in json_docs:
        click.get_text_stream('stdout', 'utf-8').write(dump_json(doc) + '\n')