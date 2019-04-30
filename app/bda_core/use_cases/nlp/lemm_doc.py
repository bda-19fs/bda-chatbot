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
    vocabular = file_as_dict(file_map[language])
    doc = (x.replace('\n', '') for x in doc)
    doc = (x for x in doc if x != '')
    return map(lambda x: lemm(x, vocabular), doc)


def lemm_doc(doc, language='de'):
    '''
        Lemms all words in doc.
    '''
    doc = list(filter(lambda x: x != '', doc))
    vocabular = file_as_dict(file_map[language])
    return list(map(lambda x: lemm(x, vocabular), doc))
