import re
import numpy as np
from nltk.stem.snowball import SnowballStemmer


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

def stemming_iterator(doc):
    for line in doc.split('\n'):
        yield None if line == '' else str.join(' ', stemm(line.split(' ')))
