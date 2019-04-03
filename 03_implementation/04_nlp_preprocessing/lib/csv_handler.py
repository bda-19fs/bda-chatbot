import pandas as pd
import pickle

def extract(file, col, out, enc, sep):
    corpus = pd.read_csv(file, sep=sep, encoding=enc, skiprows=[0], usecols=[col])
    values = corpus.values.flatten().tolist()
    pickle.dump(values, open(out, 'wb'))

    return (values[:5], len(values))
