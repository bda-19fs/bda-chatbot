import click
from os import sys, path

# add modules from parent to path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from entities.file.reader import file_as_dict
from entities.nlp.grammar import correct


def correct_grammar_stream(doc, grammar):
    grammar = file_as_dict(grammar)
    doc = list(filter(lambda x: x != '', doc.split('\n')))

    lines = 0
    for line in doc:
        corrected_line = correct(line, grammar)
        click.get_text_stream('stdout', 'utf-8').write(corrected_line + '\n')
        lines += 1
    return lines

def correct_grammar(doc, grammar='res/custom_ch_grammar.txt'):
    grammar = file_as_dict(grammar)
    doc = list(filter(lambda x: x != '', doc))
    return list(map(lambda x: correct(x, grammar), doc))
