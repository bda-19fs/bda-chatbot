from nltk.stem.snowball import SnowballStemmer
from bda_core.entities.file.reader import (
    file_as_list,
    file_as_dict
)
from bda_core.entities.nlp.normalize import normalize
from bda_core.entities.nlp.grammar import correct
from bda_core.entities.nlp.stemming import stemm
from bda_core.entities.nlp.lemming import lemm
from bda_core.entities.nlp.stopwords import remove


def nlp_strategy(config):
    config = f'{config["dataset"]}{config["algorithm"]}'
    strategy = {
        '00': stackexchange_normalize,
        '01': stackexchange_stemming,
        '02': stackexchange_lemming,
        '03': stackexchange_stopwords,
        '04': stackexchange_stopwords_stemming,
        '05': stackexchange_stopwords_lemming,
        '10': ionesoft_normalize,
        '11': ionesoft_stemming,
        '12': ionesoft_lemming,
        '13': ionesoft_stopwords,
        '14': ionesoft_stopwords_stemming,
        '15': ionesoft_stopwords_lemming
    }
    return strategy.get(config, 'unknown config')


def stackexchange_normalize(question):
    return normalize(question)


def stackexchange_stemming(question):
    question = stackexchange_normalize(question)
    stemmer = SnowballStemmer('english')
    return stemm(question, stemmer)


def stackexchange_lemming(question):
    vocabular = file_as_dict('res/custom_en_vocabular.txt')
    question = stackexchange_normalize(question)
    return lemm(question, vocabular)


def stackexchange_stopwords(question):
    stopwords = file_as_list('res/custom_en_stopwords.txt')
    question = stackexchange_normalize(question)
    return remove(question, stopwords)


def stackexchange_stopwords_stemming(question):
    question = stackexchange_stopwords(question)
    return stackexchange_stemming(question)


def stackexchange_stopwords_lemming(question):
    question = stackexchange_stopwords(question)
    return stackexchange_lemming(question)


def ionesoft_normalize(question):
    grammar = file_as_dict('res/custom_ch_grammar.txt')
    normalized = normalize(question)
    return correct(normalized, grammar)


def ionesoft_stemming(question):
    question = ionesoft_normalize(question)
    stemmer = SnowballStemmer('german')
    return stemm(question, stemmer)


def ionesoft_lemming(question):
    vocabular = file_as_dict('res/custom_ch_vocabular.txt')
    question = ionesoft_normalize(question)
    return lemm(question, vocabular)


def ionesoft_stopwords(question):
    stopwords = file_as_list('res/custom_ch_stopwords.txt')
    question = ionesoft_normalize(question)
    return remove(question, stopwords)


def ionesoft_stopwords_stemming(question):
    question = ionesoft_stopwords(question)
    return ionesoft_stemming(question)


def ionesoft_stopwords_lemming(question):
    question = ionesoft_stopwords(question)
    return ionesoft_lemming(question)
