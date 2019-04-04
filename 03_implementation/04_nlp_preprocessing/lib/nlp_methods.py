import re
import numpy as np
from nltk.stem.snowball import SnowballStemmer


def normalize(sentence):
    double_spaces = r' +'
    not_in_swiss_alphabet = r'[^\u00C0-\u017Fa-zA-Z\s]'

    sentence = re.sub(not_in_swiss_alphabet, ' ', sentence, re.I | re.A)
    sentence = re.sub(double_spaces, ' ', sentence, re.I | re.A)

    sentence = sentence.lower()
    return sentence.strip()

def normalization_iterator(doc):
    '''
        Normalizes a stdin stream by removing all characters that are
        not in the swiss alphabet.
    '''
    for line in doc.split('\n'):
        yield None if line == '' else normalize(line)


def convert_to_list(stopwords):
    with open(stopwords, 'r', encoding='utf-8') as file:
        return list(map(lambda line: line.strip(), file.readlines()))

def remove_stopwords(tokens, stop_words):
    return [token for token in tokens if token not in stop_words]

def stopwords_iterator(doc, stopwords):
    '''
        Remove stopwords in a list of strings.
    '''
    stopwords = convert_to_list(stopwords)

    for line in doc.split('\n'):
        words = line.split(' ')
        yield None if line == '' else str.join(' ', [word for word in words if word not in stopwords])


def stemm(tokens, stemmer=SnowballStemmer('german', ignore_stopwords=True)):
    return [stemmer.stem(token) for token in tokens]

def stemm_doc(token_doc):
    return list(map(lambda t: stemm(t), token_doc))
