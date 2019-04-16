def remove(line, stopwords):
    words = line.split(' ')
    return str.join(' ', [word for word in words if word not in stopwords])
