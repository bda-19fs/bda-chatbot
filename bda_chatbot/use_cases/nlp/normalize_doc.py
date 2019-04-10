import click
from os import sys, path

# add modules from parent to path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from entities.nlp.normalize import normalize


def normalize_doc(doc):
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
