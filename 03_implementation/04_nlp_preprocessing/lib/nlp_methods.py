import re
import numpy as np
from nltk.stem.snowball import SnowballStemmer


def stemm(tokens, stemmer=SnowballStemmer('german', ignore_stopwords=True)):
    return [stemmer.stem(token) for token in tokens]

def stemming_iterator(doc):
    for line in doc.split('\n'):
        yield None if line == '' else str.join(' ', stemm(line.split(' ')))
