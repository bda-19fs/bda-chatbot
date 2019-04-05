def stopwords_file_as_list(stopwords):
    with open(stopwords, 'r', encoding='utf-8') as file:
        return list(map(lambda line: line.strip(), file.readlines()))

def remove_stopwords(tokens, stop_words):
    return [token for token in tokens if token not in stop_words]

def nlp_stopwords(doc, stopwords):
    '''
        Remove stopwords in a list of strings.
    '''
    stopwords = stopwords_file_as_list(stopwords)
    doc = list(filter(lambda x: x != '', doc.split('\n')))

    lines = 0
    for line in doc:
        words = line.split(' ')
        cleaned_line = str.join(' ', [word for word in words if word not in stopwords])
        print(cleaned_line)
        lines += 1
    return lines
