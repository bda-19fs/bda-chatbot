import os


def file_as_dict(file):
    file = os.path.join(os.path.dirname(__file__), file)
    file_dict = dict()
    with open(file, 'r', encoding='utf-8') as file:
        for line in file:
            pair = line.split(',')
            file_dict[pair[0]] = pair[1].strip()

    return file_dict

def file_as_list(file):
    file = os.path.join(os.path.dirname(__file__), file)
    with open(file, 'r', encoding='utf-8') as file:
        return list(map(lambda line: line.strip(), file.readlines()))
