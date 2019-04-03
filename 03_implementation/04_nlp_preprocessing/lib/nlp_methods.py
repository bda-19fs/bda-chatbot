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

def normalize_doc(doc):
    '''
        Normalizes a list of strings by removing all characters that are
        not in the swiss alphabet.
    '''
    return list(map(lambda sentence: normalize(sentence), doc))


def tokenize_doc(doc):
    '''
        Tokenize a list of strings by spliting words by space character.
    '''
    return [sentence.split(' ') for sentence in doc]


def remove_stopwords(tokens, stop_words):
    return [token for token in tokens if token not in stop_words]

def remove_stopwords_doc(token_doc, stopwords):
    '''
        Remove stopwords in a list of strings.
    '''
    return list(map(lambda t: remove_stopwords(t, stopwords), token_doc))


def stemm(tokens, stemmer=SnowballStemmer('german', ignore_stopwords=True)):
    return [stemmer.stem(token) for token in tokens]

def stemm_doc(token_doc):
    return list(map(lambda t: stemm(t), token_doc))
