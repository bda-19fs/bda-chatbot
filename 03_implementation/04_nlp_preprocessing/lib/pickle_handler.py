import pickle


def load(extract):
    return pickle.load(open(extract, 'rb'))

def dump(object, out):
    pickle.dump(object, open(out, 'wb'))
