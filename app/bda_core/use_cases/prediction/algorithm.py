import pickle
from joblib import load
from gensim.models import Word2Vec
from bda_core.use_cases.prediction.utils import (
    predict_n_answers,
    predict_n_w2v_answers
)
from bda_core.entities.file.reader import file_as_list


def algorithm_strategy(config):
    config = f'{config["dataset"]}{config["algorithm"]}{config["domain_limit"]}'
    strategy = {
        '000': stackexchange_100,
        '001': stackexchange_95,
        '002': stackexchange_90,
        '100': ionesoft_100,
        '101': ionesoft_95,
        '102': ionesoft_90,
    }
    return strategy.get(config, 'unknown config')

def load_tags_answers(dataset):
    tags = file_as_list(f'models/{dataset}/{dataset}_tags.txt', local=False)
    answers = file_as_list(f'models/{dataset}/{dataset}_answers.txt', local=False)
    return tags, answers

stack_path = 'models/stackexchange/'
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

def ionesoft_100(question, tags, answers):
    tfidf_tags, tfidf_answers = ionesoft_tfidf_100(question, tags, answers)
    w2v_tags, w2v_answers = ionesoft_tfidf_100(question, tags, answers)
    return tfidf_tags, tfidf_answers, w2v_tags, w2v_answers

def ionesoft_95(question, tags, answers):
    tfidf_tags, tfidf_answers = ionesoft_tfidf_95(question, tags, answers)
    w2v_tags, w2v_answers = ionesoft_tfidf_95(question, tags, answers)
    return tfidf_tags, tfidf_answers, w2v_tags, w2v_answers

def ionesoft_90(question, tags, answers):
    tfidf_tags, tfidf_answers = ionesoft_tfidf_90(question, tags, answers)
    w2v_tags, w2v_answers = ionesoft_tfidf_90(question, tags, answers)
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

ione_path = 'models/ionesoft/'
def ionesoft_tfidf_100(question, tags, answers):
    language_model = load(f'{ione_path}tfidf_100_model.joblib')
    vectorizer = load(f'{ione_path}tfidf_100_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, 10)

def ionesoft_tfidf_95(question, tags, answers):
    language_model = load(f'{ione_path}tfidf_95_model.joblib')
    vectorizer = load(f'{ione_path}tfidf_95_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, 10)

def ionesoft_tfidf_90(question, tags, answers):
    language_model = load(f'{ione_path}tfidf_90_model.joblib')
    vectorizer = load(f'{ione_path}tfidf_90_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, 10)

def ionesoft_w2v_100(question, tags, answers):
    model = Word2Vec.load(f'{ione_path}w2v_100_model.w2v')
    question_vectors = pickle.load(open(f'{ione_path}w2v_100_vectors.pickle', 'rb'))
    return predict_n_w2v_answers(question, model, question_vectors, tags, answers, 10)
