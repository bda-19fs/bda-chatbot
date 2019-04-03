import re
import numpy as np


def normalize(sentence):
    double_spaces = r' +'
    not_in_swiss_alphabet = r'[^\u00C0-\u017Fa-zA-Z\s]'

    sentence = re.sub(not_in_swiss_alphabet, ' ', sentence, re.I | re.A)
    sentence = re.sub(double_spaces, ' ', sentence, re.I | re.A)

    sentence = sentence.lower()
    return sentence.strip()

def normalize_doc(doc):
    '''Normalizes a list of strings by removing all characters that are not
    in the swiss alphabet.'''
    return list(map(lambda sentence: normalize(sentence), doc))
