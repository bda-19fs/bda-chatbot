from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer


def fit_concepts(concepts):
    vectorizer = TfidfVectorizer(use_idf=True)
    X = vectorizer.fit_transform(concepts)
    return X, vectorizer

def transform_knowledge(vectorizer, questions):
    tfidf = vectorizer.transform(questions)
    return tfidf, vectorizer
