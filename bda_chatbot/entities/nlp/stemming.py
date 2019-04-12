def stemm(line, stemmer):
    tokens = line.split(' ')
    return str.join(' ', [stemmer.stem(token) for token in tokens])
