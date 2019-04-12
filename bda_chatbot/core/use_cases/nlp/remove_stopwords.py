import click
from entities.file.reader import file_as_list
from entities.nlp.stopwords import remove

def remove_stopwords_stream(doc, stopwords):
    '''
        Remove stopwords in stdin defined in a file.
    '''
    stopwords = file_as_list(stopwords)
    doc = list(filter(lambda x: x != '', doc.split('\n')))

    lines = 0
    for line in doc:
        cleaned_line = remove(line, stopwords)
        click.get_text_stream('stdout', 'utf-8').write(cleaned_line + '\n')
        lines += 1
    return lines

def remove_stopwords(doc, stopwords='res/custom_ch_stopwords.txt'):
    '''
        Remove stopwords in a list defined in a file.
    '''
    stopwords = file_as_list(stopwords)
    doc = list(filter(lambda x: x != '', doc))
    return list(map(lambda x: remove(x, stopwords), doc))
