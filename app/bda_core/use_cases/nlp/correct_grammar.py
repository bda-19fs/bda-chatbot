from bda_core.entities.file.reader import file_as_dict
from bda_core.entities.nlp.grammar import correct


def correct_grammar_stream(doc, grammar='res/custom_ch_grammar.txt'):
    doc = (x for x in doc if x != '\n')
    grammar = file_as_dict(grammar)
    return map(lambda x: correct(x, grammar), doc)


def correct_grammar(doc, grammar='res/custom_ch_grammar.txt'):
    grammar = file_as_dict(grammar)
    doc = list(filter(lambda x: x != '', doc))
    return list(map(lambda x: correct(x, grammar), doc))
