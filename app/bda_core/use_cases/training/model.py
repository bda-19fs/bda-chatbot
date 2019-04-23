from bda_core.entities.training.vectorizer import (
    fit_concepts,
    transform_knowledge
)


def create_language_model(concepts, questions):
    X, vectorizer = fit_concepts(concepts)
    language_model, vectorizer = transform_knowledge(vectorizer, questions)
    return language_model, vectorizer
