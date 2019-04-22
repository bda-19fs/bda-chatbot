from bda_core.entities.prediction.similarity import predict_closest


def readable(probs, answers):
    return [f'{p[1][0]}, {answers[p[0]]}' for p in probs]

def predict_n_answers(X, vectorizer, texts, answers, n=10):
    probs = predict_closest(X, vectorizer, texts, n)
    return readable(probs, answers)
