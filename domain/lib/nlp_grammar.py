import re
import click
from lib.extractor import file_as_dict


def correct(line, grammar):
    for k in grammar.keys():
        if k in line:
            line = re.sub(rf'\b{k}\b', grammar[k], line)

    return line

def nlp_grammar(doc, grammar):
    grammar = file_as_dict(grammar)
    doc = list(filter(lambda x: x != '', doc.split('\n')))

    lines = 0
    for line in doc:
        corrected_line = correct(line, grammar)
        click.get_text_stream('stdout', 'utf-8').write(corrected_line + '\n')
        lines += 1
    return lines
