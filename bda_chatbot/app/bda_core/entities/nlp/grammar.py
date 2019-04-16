import re


def correct(line, grammar):
    for k in grammar.keys():
        if k in line:
            line = re.sub(rf'\b{k}\b', grammar[k], line)

    return line
