import click
from nltk.stem.snowball import SnowballStemmer
from bda_core.entities.file.reader import file_as_dict
from bda_core.entities.nlp.stemming import stemm

stemm_dic = {
    'de': 'german',
    'en': 'english'
}


def stemm_doc_stream(doc, language):
    '''
        Stemms all words in stdin stream.
    '''
    doc = list(filter(lambda x: x != '', doc.split('\n')))
    stemmer = SnowballStemmer(stemm_dic[language])

    lines = 0
    for line in doc:
        stemmed_line = stemm(line, stemmer)
        click.get_text_stream('stdout', 'utf-8').write(stemmed_line + '\n')
        lines += 1
    return lines


def stemm_doc(doc, language):
    '''
        Stemms all words in stdin stream.
    '''
    doc = list(filter(lambda x: x != '', doc))
    stemmer = SnowballStemmer(stemm_dic[language])
    return list(map(lambda x: stemm(x, stemmer), doc))


def stemm_json(json_doc, text_key, language):
    '''
    Stemms all words in a single text property of the json document.
    :param json_doc: The json document
    :param text_key: The key of the text property
    :param language: The language key of the stemmer
    :return: The json document with stemms
    '''
    stemmer = SnowballStemmer(stemm_dic[language])
    json_doc[text_key] = stemm(json_doc[text_key], stemmer)
    return json_doc
