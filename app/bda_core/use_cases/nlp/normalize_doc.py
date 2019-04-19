import click
from bda_core.entities.nlp.normalize import normalize
from bda_core.entities.file.json_handler import dump_json


def normalize_doc_stream(doc):
    '''
        Normalizes a stdin stream by removing all characters that are
        not in the swiss alphabet.
    '''
    doc = list(filter(lambda x: x != '', doc.split('\n')))

    lines = 0
    for line in doc:
        normalized_line = normalize(line)
        click.get_text_stream('stdout', 'utf-8').write(normalized_line + '\n')
        lines += 1
    return lines

def normalize_json_stream(json_docs, text_key='text'):
    '''
    Normalizes a stdin stream of a json document by removing all characters that are
    not in the swiss alphabet.
    '''
    for doc in json_docs:
        doc[text_key] = normalize(doc[text_key])
        click.get_text_stream('stdout', 'utf-8').write(dump_json(doc) + '\n')

def normalize_doc(doc):
    '''
        Normalizes a list by removing all characters that are
        not in the swiss alphabet.
    '''
    doc = list(filter(lambda x: x != '', doc))
    return list(map(lambda x: normalize(x), doc))


def normalize_json(json_doc, text_key='text'):
    '''
    Normalizes the content of one json property.
    :param json_doc: The json document
    :param text_key: The key of the text property
    :return: Normalized json document
    '''
    json_doc[text_key] = normalize(json_doc[text_key])
    return json_doc
