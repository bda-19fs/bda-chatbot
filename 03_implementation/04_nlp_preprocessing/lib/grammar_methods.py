import re


def convert_to_dict(grammar):
    grammar_dict = dict()

    with open(grammar, 'r') as file:
        for line in file:
            pair = line.split(',')
            grammar_dict[pair[0]] = pair[1].strip()

    return grammar_dict

def correct(line, grammar):
    for k in grammar.keys():
        if k in line:
            line = re.sub(rf'\b{k}\b', grammar[k], line)

    return line

def correction_iterator(doc, grammar):
    grammar = convert_to_dict(grammar)

    for line in doc.split('\n'):
        yield None if line == '' else correct(line, grammar)
