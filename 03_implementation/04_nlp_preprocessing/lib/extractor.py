import click


def extractor(csv, column, separator):
    csv = list(filter(lambda x: x != '', csv.split('\n')))

    lines = 0
    for line in csv:
        extracted_column = line.split(separator)[column]
        click.get_text_stream('stdout', 'utf-8').write(extracted_column + '\n')
    return lines

def file_as_dict(file):
    file_dict = dict()

    with open(file, 'r', encoding='utf-8') as file:
        for line in file:
            pair = line.split(',')
            file_dict[pair[0]] = pair[1].strip()

    return file_dict

def file_as_list(file):
    with open(file, 'r', encoding='utf-8') as file:
        return list(map(lambda line: line.strip(), file.readlines()))
