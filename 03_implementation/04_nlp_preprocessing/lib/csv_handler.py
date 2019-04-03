import pandas as pd


def extract(file, col, out, enc, sep):
    corpus = pd.read_csv(file, sep=sep, encoding=enc, usecols=[col])
    return corpus.values.flatten().tolist()
