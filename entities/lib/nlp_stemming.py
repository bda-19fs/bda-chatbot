import re
import click
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
        click.get_text_stream('stdout', 'utf-8').write(stemmed_line + '\n')
        lines += 1
    return lines
