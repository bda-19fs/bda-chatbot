import re


def lemm(line, vocabular):
    for k in vocabular.keys():
        if k in line:
            line = re.sub(rf'\b{k}\b', vocabular[k], line)
    return line
