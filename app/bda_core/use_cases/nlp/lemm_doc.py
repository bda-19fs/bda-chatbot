import click
from bda_core.entities.file.reader import file_as_dict
from bda_core.entities.nlp.lemming import lemm

file_map = {
    'de': 'res/custom_ch_vocabular.txt',
    'en': 'res/custom_en_vocabular.txt'
}

def lemm_doc_stream(doc, language):
    '''
        Lemms all words in stdin stream.
    '''
    doc = lemm_doc(doc.split('\n'), language)
    [click.get_text_stream('stdout', 'utf-8').write(line + '\n') for line in doc]
    return len(doc)

def lemm_doc(doc, language='de'):
    '''
        Lemms all words in doc.
    '''
    doc = list(filter(lambda x: x != '', doc))
    vocabular = file_as_dict(file_map[language])
    return list(map(lambda x: lemm(x, vocabular), doc))
