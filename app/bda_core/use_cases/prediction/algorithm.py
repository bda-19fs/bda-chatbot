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
        '000': stackexchange_tfidf_100,
        '001': stackexchange_tfidf_85,
        '002': stackexchange_tfidf_75,
        '060': stackexchange_w2v_100
    }
    return strategy.get(config, 'unknown config')

stack_path = 'models/stackexchange/'
def load_tags_answers():
    tags = file_as_list(f'{stack_path}stackexchange_tags.txt')
    answers = file_as_list(f'{stack_path}stackexchange_answers.txt')
    return tags, answers

def stackexchange_tfidf_100(question, tags, answers):
    language_model = load(f'{stack_path}tfidf_100_model.joblib')
    vectorizer = load(f'{stack_path}tfidf_100_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, 10)

def stackexchange_tfidf_85(question, tags, answers):
    language_model = load(f'{stack_path}tfidf_85_model.joblib')
    vectorizer = load(f'{stack_path}tfidf_85_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, 10)

def stackexchange_tfidf_75(question, tags, answers):
    language_model = load(f'{stack_path}tfidf_75_model.joblib')
    vectorizer = load(f'{stack_path}tfidf_75_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, 10)

def stackexchange_w2v_100(question, tags, answers):
    model = Word2Vec.load(f'{stack_path}w2v_100_model.w2v')
    question_vectors = pickle.load(open(f'{stack_path}w2v_100_vectors.pickle', 'rb'))
    return predict_n_w2v_answers(question, model, question_vectors, tags, answers, 10)
