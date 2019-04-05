import re
import click


def normalize(sentence):
    double_spaces = r' +'
    not_in_swiss_alphabet = r'[^\u00C0-\u017Fa-zA-Z\s]'

    sentence = re.sub(not_in_swiss_alphabet, ' ', sentence, re.I | re.A)
    sentence = re.sub(double_spaces, ' ', sentence, re.I | re.A)

    sentence = sentence.lower()
    return sentence.strip()

def nlp_normalize(doc):
    '''
        Normalizes a stdin stream by removing all characters that are
        not in the swiss alphabet.
    '''
    doc = list(filter(lambda x: x != '', doc.split('\n')))

    lines = 0
    for line in doc:
        normalized_line = normalize(line)
        click.get_text_stream('stdout', 'utf-8').write(normalized_line + '\n')
        lines += 1
    return lines
