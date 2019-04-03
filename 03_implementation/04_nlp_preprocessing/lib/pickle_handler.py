import pickle


def load(extract):
    return pickle.load(open(extract, 'rb'))
