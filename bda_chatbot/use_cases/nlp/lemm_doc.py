import click
import spacy
from os import sys, path

# add modules from parent to path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from entities.file.reader import file_as_dict
from entities.nlp.lemming import lemm

file_map = {
    'de': 'res/custom_ch_vocabular.txt',
    'en': 'res/custom_en_vocabular.txt'
}

def lemm_doc_stream(doc, language):
    '''
        Lemms all words in stdin stream.
    '''
    doc = list(filter(lambda x: x != '', doc.split('\n')))
    vocabular = file_as_dict(file_map[language])

    lines = 0
    for line in doc:
        lemmed_line = lemm(line, vocabular)
        click.get_text_stream('stdout', 'utf-8').write(lemmed_line + '\n')
        lines += 1
    return lines

def lemm_doc(doc, language='de'):
    '''
        Lemms all words in doc.
    '''
    doc = list(filter(lambda x: x != '', doc))
    vocabular = file_as_dict(file_map[language])
    return list(map(lambda x: lemm(x, vocabular), doc))
