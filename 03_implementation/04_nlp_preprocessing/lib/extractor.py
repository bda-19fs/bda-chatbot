import click


def extractor(csv, column, separator):
    csv = list(filter(lambda x: x != '', csv.split('\n')))

    lines = 0
    for line in csv:
        extracted_column = line.split(separator)[column]
        click.get_text_stream('stdout', 'utf-8').write(extracted_column + '\n')
    return lines
