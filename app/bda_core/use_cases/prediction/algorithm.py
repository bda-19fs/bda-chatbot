import pickle
from joblib import load
from gensim.models import Word2Vec
from bda_core.use_cases.prediction.utils import (
    predict_n_answers,
    predict_n_w2v_answers
)


def file_as_list(file):
    with open(file, 'r', encoding='utf-8') as file:
        return list(map(lambda line: line.strip(), file.readlines()))

def algorithm_strategy(config):
    config = f'{config["dataset"]}{config["algorithm"]}{config["domain_limit"]}'
    strategy = {
        '000': stackexchange_100,
        '001': stackexchange_95,
        '002': stackexchange_90
    }
    return strategy.get(config, 'unknown config')

stack_path = 'models/stackexchange/'
def load_tags_answers():
    tags = file_as_list(f'{stack_path}stackexchange_tags.txt')
    answers = file_as_list(f'{stack_path}stackexchange_answers.txt')
    return tags, answers

def stackexchange_100(question, tags, answers):
    tfidf_tags, tfidf_answers = stackexchange_tfidf_100(question, tags, answers)
    w2v_tags, w2v_answers = stackexchange_w2v_100(question, tags, answers)
    return tfidf_tags, tfidf_answers, w2v_tags, w2v_answers

def stackexchange_95(question, tags, answers):
    tfidf_tags, tfidf_answers = stackexchange_tfidf_95(question, tags, answers)
    w2v_tags, w2v_answers = stackexchange_w2v_100(question, tags, answers)
    return tfidf_tags, tfidf_answers, w2v_tags, w2v_answers

def stackexchange_90(question, tags, answers):
    tfidf_tags, tfidf_answers = stackexchange_tfidf_90(question, tags, answers)
    w2v_tags, w2v_answers = stackexchange_w2v_100(question, tags, answers)
    return tfidf_tags, tfidf_answers, w2v_tags, w2v_answers

def stackexchange_tfidf_100(question, tags, answers):
    language_model = load(f'{stack_path}tfidf_100_model.joblib')
    vectorizer = load(f'{stack_path}tfidf_100_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, 10)

def stackexchange_tfidf_95(question, tags, answers):
    language_model = load(f'{stack_path}tfidf_95_model.joblib')
    vectorizer = load(f'{stack_path}tfidf_95_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, 10)

def stackexchange_tfidf_90(question, tags, answers):
    language_model = load(f'{stack_path}tfidf_90_model.joblib')
    vectorizer = load(f'{stack_path}tfidf_90_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, 10)

def stackexchange_w2v_100(question, tags, answers):
    model = Word2Vec.load(f'{stack_path}w2v_100_model.w2v')
    question_vectors = pickle.load(open(f'{stack_path}w2v_100_vectors.pickle', 'rb'))
    return predict_n_w2v_answers(question, model, question_vectors, tags, answers, 10)
