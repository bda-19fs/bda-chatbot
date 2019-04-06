import click
from lib.extractor import file_as_list


def remove_stopwords(tokens, stop_words):
    return [token for token in tokens if token not in stop_words]

def nlp_stopwords(doc, stopwords):
    '''
        Remove stopwords in a list of strings.
    '''
    stopwords = file_as_list(stopwords)
    doc = list(filter(lambda x: x != '', doc.split('\n')))

    lines = 0
    for line in doc:
        words = line.split(' ')
        cleaned_line = str.join(' ', [word for word in words if word not in stopwords])
        click.get_text_stream('stdout', 'utf-8').write(cleaned_line + '\n')
        lines += 1
    return lines
