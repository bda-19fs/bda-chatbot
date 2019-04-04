def csv_iterator(csv, column, seperator):
    for line in csv.split('\n'):
        yield '' if line == '' else line.split(seperator)[column]
