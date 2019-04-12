import click
from entities.nlp.normalize import normalize


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

def normalize_doc(doc):
    '''
        Normalizes a list by removing all characters that are
        not in the swiss alphabet.
    '''
    doc = list(filter(lambda x: x != '', doc))
    return list(map(lambda x: normalize(x), doc))
