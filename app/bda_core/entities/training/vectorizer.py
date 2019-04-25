from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer


def fit_concepts(concepts, domain_limit):
    min_df = 1 if domain_limit == 0 else domain_limit # default is int 1
    max_df = 1.0 - domain_limit # default is float 1.0
    vectorizer = TfidfVectorizer(use_idf=True, min_df=min_df, max_df=max_df)
    X = vectorizer.fit_transform(concepts)
    return X, vectorizer

def transform_knowledge(vectorizer, questions):
    tfidf = vectorizer.transform(questions)
    return tfidf, vectorizer
