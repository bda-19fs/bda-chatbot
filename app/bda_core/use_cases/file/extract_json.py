import click
from bda_core.entities.file.json_handler import from_str_to_json, dump_json


def extract_json_documents(doc):
    '''
    Extracts json documents from a raw data bulk.
    The input data must be in this format. Each json document has to be on a new line.

    {"some":"json"}
    {"some":"other json"}
    ...

    :param doc: The input data
    :return: A python list of json documents
    '''
    doc = list(filter(lambda x: x != '', doc.split('\n')))
    json_data = [extract_json_document(line) for line in doc]
    return json_data


def extract_json_document(doc):
    '''
    Extracts one json document from the given input string.
    :param doc: The input string that represents a json document
    :return: A python dict
    '''
    return from_str_to_json(doc)


def write_json_docs_out(json_docs):
    '''
    Writes a list of json documents to the stdout stream.
    :param json_docs: A python list of json documents
    '''
    for doc in json_docs:
        write_json_doc_out(doc)


def write_json_doc_out(json_doc):
    '''
    Writes a single json document to the stdout stream.
    :param json_doc: A python dict
    '''
    click.get_text_stream('stdout', 'utf-8').write(dump_json(json_doc) + '\n')
