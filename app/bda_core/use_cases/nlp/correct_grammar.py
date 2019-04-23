import click
from bda_core.entities.file.reader import file_as_dict
from bda_core.entities.nlp.grammar import correct


def correct_grammar_stream(doc, grammar='res/custom_ch_grammar.txt'):
    doc = correct_grammar(doc.split('\n'), grammar)
    [click.get_text_stream('stdout', 'utf-8').write(line + '\n') for line in doc]
    return len(doc)

def correct_grammar(doc, grammar='res/custom_ch_grammar.txt'):
    grammar = file_as_dict(grammar)
    doc = list(filter(lambda x: x != '', doc))
    return list(map(lambda x: correct(x, grammar), doc))
