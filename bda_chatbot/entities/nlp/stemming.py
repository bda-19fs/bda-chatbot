from nltk.stem.snowball import SnowballStemmer


def stemm(line, stemmer=SnowballStemmer('german', ignore_stopwords=True)):
    tokens = line.split(' ')
    return str.join(' ', [stemmer.stem(token) for token in tokens])
