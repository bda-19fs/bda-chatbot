import click
from bda_core.entities.file.reader import file_as_list
from bda_core.entities.nlp.stopwords import remove
from bda_core.entities.file.json_handler import dump_json


def remove_stopwords_stream(doc, stopwords):
    '''
        Remove stopwords in stdin defined in a file.
    '''
    stopwords = file_as_list(stopwords)
    doc = list(filter(lambda x: x != '', doc.split('\n')))

    lines = 0
    for line in doc:
        cleaned_line = remove(line, stopwords)
        click.get_text_stream('stdout', 'utf-8').write(cleaned_line + '\n')
        lines += 1
    return lines


def remove_stopwords_json_stream(json_docs, stopwords, text_key='text'):
    '''
    Removes stopwords in stdin defined as json documents.
    '''
    stopwords = file_as_list(stopwords)
    for doc in json_docs:
        doc[text_key] = remove(doc[text_key], stopwords)
        click.get_text_stream('stdout', 'utf-8').write(dump_json(doc) + '\n')


def remove_stopwords(doc, stopwords='res/custom_ch_stopwords.txt'):
    '''
        Remove stopwords in a list defined in a file.
    '''
    stopwords = file_as_list(stopwords)
    doc = list(filter(lambda x: x != '', doc))
    return list(map(lambda x: remove(x, stopwords), doc))


def remove_stopwords_json(json_doc, text_key, stopwords='res/custom_ch_stopwords.txt'):
    '''
    Remove stopwords in a single text property of the json document.
    :param json_doc: The json document
    :param text_key: The key of the text property
    :param stopwords: The filepath to a stop word list
    :return: The json document without stop words
    '''
    stopwords = file_as_list(stopwords)
    json_doc[text_key] = remove(json_doc[text_key], stopwords)
    return json_doc
