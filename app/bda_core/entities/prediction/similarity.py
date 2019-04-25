from sklearn.metrics.pairwise import cosine_similarity


def getKey(item):
    return item[1]


def predict_closest(X, vectorizer, texts, n):
    probs = predict_closest_vectors(X, vectorizer.transform(
        texts
    ))
    return probs[:n]


def predict_closest_vectors(X, pre_calculated_vectors):
    probs = cosine_similarity(X, pre_calculated_vectors)
    return sorted(list(enumerate(probs)), key=getKey, reverse=True)


def predict_closest_w2v(X, pre_calculated_vectors):
    probs = []
    for vec in pre_calculated_vectors:
        probs.append(cosine_similarity([X], [vec]))
    return sorted(list(enumerate(probs)), key=getKey, reverse=True)
