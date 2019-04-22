from sklearn.metrics.pairwise import cosine_similarity


def getKey(item):
    return item[1]

def predict_closest(X, vectorizer, texts, n):
    probs = cosine_similarity(X, vectorizer.transform(
        texts
    ))
    return sorted(list(enumerate(probs)), key=getKey, reverse=True)[:n]
