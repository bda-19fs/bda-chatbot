from bda_core.entities.training.vectorizer import (
    fit_concepts,
    transform_knowledge
)
import bda_core.entities.training.word2vec_trainer as w2v


def create_language_model(concepts, questions, domain_limit):
    X, vectorizer = fit_concepts(concepts, domain_limit)
    language_model, vectorizer = transform_knowledge(vectorizer, questions)
    return language_model, vectorizer


def create_w2v_model(sentences, questions, config=w2v.Config()):
    model = w2v.fit_model(sentences, config)
    vectors = w2v.create_sentence_vectors(model, questions)
    vectors = w2v.create_matrix_from_vectors(vectors)
    return model, vectors
