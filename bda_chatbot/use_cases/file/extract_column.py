import click


def extract_column_stream(csv, column, separator):
    '''
        Extract a column from a stdin stream.
    '''
    csv = list(filter(lambda x: x != '', csv.split('\n')))

    lines = 0
    for line in csv:
        extracted_column = line.split(separator)[column]
        click.get_text_stream('stdout', 'utf-8').write(extracted_column + '\n')
        lines += 1
    return lines

def extract_column(csv, column, separator):
    '''
        Extract a column from a list.
    '''
    csv = list(filter(lambda x: x != '', csv))
    return list(map(lambda x: x.split(separator)[column], csv))
