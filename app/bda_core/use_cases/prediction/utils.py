from bda_core.entities.prediction.similarity import (
    predict_closest,
    predict_closest_vectors,
    predict_closest_w2v
)
from bda_core.entities.training.word2vec_trainer import avg_word_vector, transpose_vector


def readable(probs, answers):
    return [f'{p[1][0]}, {answers[p[0]]}' for p in probs]

def readable_w2v(probs, answers):
    return [f'{p[1][0]}, {answers[p[0]]}' for p in probs]

def predict_n_answers(X, vectorizer, texts, tags, answers, questions, n=10):
    probs = predict_closest(X, vectorizer, texts, n)
    return readable(probs, tags), readable(probs, answers), readable(probs, questions)

def predict_n_w2v_answers(question, model, question_vectors, tags, answers, questions, n=10):
    X = avg_word_vector(model, question.split(' '))
    X = transpose_vector(X)
    probs = predict_closest_w2v(X, question_vectors)
    return readable_w2v(probs[:n], tags), readable_w2v(probs[:n], answers), readable_w2v(probs[:n], questions)
