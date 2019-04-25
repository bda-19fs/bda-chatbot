from bda_core.entities.prediction.similarity import (
    predict_closest,
    predict_closest_vectors
)
from bda_core.entities.training.word2vec_trainer import avg_word_vector


def readable(probs, answers):
    return [f'{p[1][0]}, {answers[p[0]]}' for p in probs]

def predict_n_answers(X, vectorizer, texts, tags, answers, n=10):
    probs = predict_closest(X, vectorizer, texts, n)
    return readable(probs, tags), readable(probs, answers)

def predict_n_w2v_answers(question, model, question_vectors, tags, answers, n=10):
    X = avg_word_vector(model, question.split(' '))
    probs = predict_closest_vectors(X, question_vectors)
    return readable(probs[:n], tags), readable(probs[:n], answers)
