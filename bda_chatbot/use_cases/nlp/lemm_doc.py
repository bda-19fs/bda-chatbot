import click
from os import sys, path

# add modules from parent to path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from entities.file.reader import file_as_dict
from entities.nlp.lemming import lemm


def lemm_doc(doc, vocabular):
    '''
        Lemms all words in doc.
    '''
    doc = list(filter(lambda x: x != '', doc.split('\n')))
    vocabular = file_as_dict(vocabular)

    lines = 0
    for line in doc:
        lemmed_line = lemm(line, vocabular)
        click.get_text_stream('stdout', 'utf-8').write(lemmed_line + '\n')
        lines += 1
    return lines
