import click
from os import sys, path

# add modules from parent to path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from entities.file.reader import file_as_dict
from entities.nlp.stemming import stemm


def stemm_doc_stream(doc):
    '''
        Stemms all words in stdin stream.
    '''
    doc = list(filter(lambda x: x != '', doc.split('\n')))

    lines = 0
    for line in doc:
        stemmed_line = stemm(line)
        click.get_text_stream('stdout', 'utf-8').write(stemmed_line + '\n')
        lines += 1
    return lines

def stemm_doc(doc):
    '''
        Stemms all words in stdin stream.
    '''
    doc = list(filter(lambda x: x != '', doc))
    return list(map(lambda x: stemm(x), doc))
