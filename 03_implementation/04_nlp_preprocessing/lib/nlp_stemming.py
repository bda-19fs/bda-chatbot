import re
from nltk.stem.snowball import SnowballStemmer


def stemm(tokens, stemmer=SnowballStemmer('german', ignore_stopwords=True)):
    return [stemmer.stem(token) for token in tokens]

def nlp_stemming(doc):
    '''
        Stemms all words in doc.
    '''
    doc = list(filter(lambda x: x != '', doc.split('\n')))

    lines = 0
    for line in doc:
        stemmed_line = str.join(' ', stemm(line.split(' ')))
        print(stemmed_line)
        lines += 1
    return lines
