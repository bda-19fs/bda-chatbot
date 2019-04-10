import re
import click
from lib.extractor import file_as_dict


def lemm(line, vocabular):
    for k in vocabular.keys():
        if k in line:
            line = re.sub(rf'\b{k}\b', vocabular[k], line)
    return line

def nlp_lemming(doc, vocabular):
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
