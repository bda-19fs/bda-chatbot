import pickle

from gensim.models import Word2Vec
from joblib import load

from bda_core.entities.file.reader import file_as_list
from bda_core.use_cases.prediction.utils import (
    predict_n_answers,
    predict_n_w2v_answers
)


def algorithm_strategy(config):
    config = f'{config["dataset"]}{config["algorithm"]}{config["domain_limit"]}'
    strategy = {
        '000': stackexchange_100,
        '001': stackexchange_95,
        '002': stackexchange_90,
        '010': stackexchange_stemming_100,
        '011': stackexchange_stemming_95,
        '012': stackexchange_stemming_90,
        '020': stackexchange_lemming_100,
        '021': stackexchange_lemming_95,
        '022': stackexchange_lemming_90,
        '030': stackexchange_stopwords_100,
        '031': stackexchange_stopwords_95,
        '032': stackexchange_stopwords_90,
        '040': stackexchange_stopwords_stemming_100,
        '041': stackexchange_stopwords_stemming_95,
        '042': stackexchange_stopwords_stemming_90,
        '050': stackexchange_stopwords_lemming_100,
        '051': stackexchange_stopwords_lemming_95,
        '052': stackexchange_stopwords_lemming_90,
        '100': ionesoft_100,
        '101': ionesoft_95,
        '102': ionesoft_90,
        '110': ionesoft_stemming_100,
        '111': ionesoft_stemming_95,
        '112': ionesoft_stemming_90,
        '120': ionesoft_lemming_100,
        '121': ionesoft_lemming_95,
        '122': ionesoft_lemming_90,
        '130': ionesoft_stopwords_100,
        '131': ionesoft_stopwords_95,
        '132': ionesoft_stopwords_90,
        '140': ionesoft_stopwords_stemming_100,
        '141': ionesoft_stopwords_stemming_95,
        '142': ionesoft_stopwords_stemming_90,
        '150': ionesoft_stopwords_lemming_100,
        '151': ionesoft_stopwords_lemming_95,
        '152': ionesoft_stopwords_lemming_90
    }
    return strategy.get(config, 'unknown config')


def load_tags_answers(dataset):
    tags = file_as_list(f'models/{dataset}/{dataset}_tags.txt', local=False)
    answers = file_as_list(f'models/{dataset}/{dataset}_answers.txt', local=False)
    questions = file_as_list(f'models/{dataset}/{dataset}_questions.txt', local=False)
    return tags, answers, questions


stack_path = 'models/stackexchange/'


def stackexchange_100(question, tags, answers, questions):
    tfidf_tags, tfidf_answers, tfidf_questions = stackexchange_tfidf_100(question, tags, answers, questions)
    w2v_tags, w2v_answers, w2v_questions = stackexchange_w2v_100(question, tags, answers, questions)
    return tfidf_tags, tfidf_answers, tfidf_questions, w2v_tags, w2v_answers, w2v_questions


def stackexchange_95(question, tags, answers, questions):
    tfidf_tags, tfidf_answers, tfidf_questions = stackexchange_tfidf_95(question, tags, answers, questions)
    w2v_tags, w2v_answers, w2v_questions = stackexchange_w2v_100(question, tags, answers, questions)
    return tfidf_tags, tfidf_answers, tfidf_questions, w2v_tags, w2v_answers, w2v_questions


def stackexchange_90(question, tags, answers, questions):
    tfidf_tags, tfidf_answers, tfidf_questions = stackexchange_tfidf_90(question, tags, answers, questions)
    w2v_tags, w2v_answers, w2v_questions = stackexchange_w2v_100(question, tags, answers, questions)
    return tfidf_tags, tfidf_answers, tfidf_questions, w2v_tags, w2v_answers, w2v_questions


def stackexchange_stemming_100(question, tags, answers, questions):
    tfidf_tags, tfidf_answers, tfidf_questions = stackexchange_stemming_tfidf_100(question, tags, answers, questions)
    w2v_tags, w2v_answers, w2v_questions = stackexchange_w2v_100(question, tags, answers, questions)
    return tfidf_tags, tfidf_answers, tfidf_questions, w2v_tags, w2v_answers, w2v_questions


def stackexchange_stemming_95(question, tags, answers, questions):
    tfidf_tags, tfidf_answers, tfidf_questions = stackexchange_stemming_tfidf_95(question, tags, answers, questions)
    w2v_tags, w2v_answers, w2v_questions = stackexchange_w2v_100(question, tags, answers, questions)
    return tfidf_tags, tfidf_answers, tfidf_questions, w2v_tags, w2v_answers, w2v_questions


def stackexchange_stemming_90(question, tags, answers, questions):
    tfidf_tags, tfidf_answers, tfidf_questions = stackexchange_stemming_tfidf_90(question, tags, answers, questions)
    w2v_tags, w2v_answers, w2v_questions = stackexchange_w2v_100(question, tags, answers, questions)
    return tfidf_tags, tfidf_answers, tfidf_questions, w2v_tags, w2v_answers, w2v_questions


def stackexchange_lemming_100(question, tags, answers, questions):
    tfidf_tags, tfidf_answers, tfidf_questions = stackexchange_lemming_tfidf_100(question, tags, answers, questions)
    w2v_tags, w2v_answers, w2v_questions = stackexchange_w2v_100(question, tags, answers, questions)
    return tfidf_tags, tfidf_answers, tfidf_questions, w2v_tags, w2v_answers, w2v_questions


def stackexchange_lemming_95(question, tags, answers, questions):
    tfidf_tags, tfidf_answers, tfidf_questions = stackexchange_lemming_tfidf_95(question, tags, answers, questions)
    w2v_tags, w2v_answers, w2v_questions = stackexchange_w2v_100(question, tags, answers, questions)
    return tfidf_tags, tfidf_answers, tfidf_questions, w2v_tags, w2v_answers, w2v_questions


def stackexchange_lemming_90(question, tags, answers, questions):
    tfidf_tags, tfidf_answers, tfidf_questions = stackexchange_lemming_tfidf_90(question, tags, answers, questions)
    w2v_tags, w2v_answers, w2v_questions = stackexchange_w2v_100(question, tags, answers, questions)
    return tfidf_tags, tfidf_answers, tfidf_questions, w2v_tags, w2v_answers, w2v_questions


def stackexchange_stopwords_100(question, tags, answers, questions):
    tfidf_tags, tfidf_answers, tfidf_questions = stackexchange_stopwords_tfidf_100(question, tags, answers, questions)
    w2v_tags, w2v_answers, w2v_questions = stackexchange_w2v_100(question, tags, answers, questions)
    return tfidf_tags, tfidf_answers, tfidf_questions, w2v_tags, w2v_answers, w2v_questions


def stackexchange_stopwords_95(question, tags, answers, questions):
    tfidf_tags, tfidf_answers, tfidf_questions = stackexchange_stopwords_tfidf_95(question, tags, answers, questions)
    w2v_tags, w2v_answers, w2v_questions = stackexchange_w2v_100(question, tags, answers, questions)
    return tfidf_tags, tfidf_answers, tfidf_questions, w2v_tags, w2v_answers, w2v_questions


def stackexchange_stopwords_90(question, tags, answers, questions):
    tfidf_tags, tfidf_answers, tfidf_questions = stackexchange_stopwords_tfidf_90(question, tags, answers, questions)
    w2v_tags, w2v_answers, w2v_questions = stackexchange_w2v_100(question, tags, answers, questions)
    return tfidf_tags, tfidf_answers, tfidf_questions, w2v_tags, w2v_answers, w2v_questions


def stackexchange_stopwords_stemming_100(question, tags, answers, questions):
    tfidf_tags, tfidf_answers, tfidf_questions = stackexchange_stopwords_stemming_tfidf_100(question, tags, answers, questions)
    w2v_tags, w2v_answers, w2v_questions = stackexchange_w2v_100(question, tags, answers, questions)
    return tfidf_tags, tfidf_answers, tfidf_questions, w2v_tags, w2v_answers, w2v_questions


def stackexchange_stopwords_stemming_95(question, tags, answers, questions):
    tfidf_tags, tfidf_answers, tfidf_questions = stackexchange_stopwords_stemming_tfidf_95(question, tags, answers, questions)
    w2v_tags, w2v_answers, w2v_questions = stackexchange_w2v_100(question, tags, answers, questions)
    return tfidf_tags, tfidf_answers, tfidf_questions, w2v_tags, w2v_answers, w2v_questions


def stackexchange_stopwords_stemming_90(question, tags, answers, questions):
    tfidf_tags, tfidf_answers, tfidf_questions = stackexchange_stopwords_stemming_tfidf_90(question, tags, answers, questions)
    w2v_tags, w2v_answers, w2v_questions = stackexchange_w2v_100(question, tags, answers, questions)
    return tfidf_tags, tfidf_answers, tfidf_questions, w2v_tags, w2v_answers, w2v_questions


def stackexchange_stopwords_lemming_100(question, tags, answers, questions):
    tfidf_tags, tfidf_answers, tfidf_questions = stackexchange_stopwords_lemming_tfidf_100(question, tags, answers, questions)
    w2v_tags, w2v_answers, w2v_questions = stackexchange_w2v_100(question, tags, answers, questions)
    return tfidf_tags, tfidf_answers, tfidf_questions, w2v_tags, w2v_answers, w2v_questions


def stackexchange_stopwords_lemming_95(question, tags, answers, questions):
    tfidf_tags, tfidf_answers, tfidf_questions = stackexchange_stopwords_lemming_tfidf_95(question, tags, answers, questions)
    w2v_tags, w2v_answers, w2v_questions = stackexchange_w2v_100(question, tags, answers, questions)
    return tfidf_tags, tfidf_answers, tfidf_questions, w2v_tags, w2v_answers, w2v_questions


def stackexchange_stopwords_lemming_90(question, tags, answers, questions):
    tfidf_tags, tfidf_answers, tfidf_questions = stackexchange_stopwords_lemming_tfidf_90(question, tags, answers, questions)
    w2v_tags, w2v_answers, w2v_questions = stackexchange_w2v_100(question, tags, answers, questions)
    return tfidf_tags, tfidf_answers, tfidf_questions, w2v_tags, w2v_answers, w2v_questions


def ionesoft_100(question, tags, answers, questions):
    tfidf_tags, tfidf_answers, tfidf_questions = ionesoft_tfidf_100(question, tags, answers, questions)
    w2v_tags, w2v_answers, w2v_questions = ionesoft_w2v_100(question, tags, answers, questions)
    return tfidf_tags, tfidf_answers, tfidf_questions, w2v_tags, w2v_answers, w2v_questions


def ionesoft_95(question, tags, answers, questions):
    tfidf_tags, tfidf_answers, tfidf_questions = ionesoft_tfidf_95(question, tags, answers, questions)
    w2v_tags, w2v_answers, w2v_questions = ionesoft_w2v_100(question, tags, answers, questions)
    return tfidf_tags, tfidf_answers, tfidf_questions, w2v_tags, w2v_answers, w2v_questions


def ionesoft_90(question, tags, answers, questions):
    tfidf_tags, tfidf_answers, tfidf_questions = ionesoft_tfidf_90(question, tags, answers, questions)
    w2v_tags, w2v_answers, w2v_questions = ionesoft_w2v_100(question, tags, answers, questions)
    return tfidf_tags, tfidf_answers, tfidf_questions, w2v_tags, w2v_answers, w2v_questions


def ionesoft_stemming_100(question, tags, answers, questions):
    tfidf_tags, tfidf_answers, tfidf_questions = ionesoft_stemming_tfidf_100(question, tags, answers, questions)
    w2v_tags, w2v_answers, w2v_questions = ionesoft_w2v_100(question, tags, answers, questions)
    return tfidf_tags, tfidf_answers, tfidf_questions, w2v_tags, w2v_answers, w2v_questions


def ionesoft_stemming_95(question, tags, answers, questions):
    tfidf_tags, tfidf_answers, tfidf_questions = ionesoft_stemming_tfidf_95(question, tags, answers, questions)
    w2v_tags, w2v_answers, w2v_questions = ionesoft_w2v_100(question, tags, answers, questions)
    return tfidf_tags, tfidf_answers, tfidf_questions, w2v_tags, w2v_answers, w2v_questions


def ionesoft_stemming_90(question, tags, answers, questions):
    tfidf_tags, tfidf_answers, tfidf_questions = ionesoft_stemming_tfidf_90(question, tags, answers, questions)
    w2v_tags, w2v_answers, w2v_questions = ionesoft_w2v_100(question, tags, answers, questions)
    return tfidf_tags, tfidf_answers, tfidf_questions, w2v_tags, w2v_answers, w2v_questions


def ionesoft_lemming_100(question, tags, answers, questions):
    tfidf_tags, tfidf_answers, tfidf_questions = ionesoft_lemming_tfidf_100(question, tags, answers, questions)
    w2v_tags, w2v_answers, w2v_questions = ionesoft_w2v_100(question, tags, answers, questions)
    return tfidf_tags, tfidf_answers, tfidf_questions, w2v_tags, w2v_answers, w2v_questions


def ionesoft_lemming_95(question, tags, answers, questions):
    tfidf_tags, tfidf_answers, tfidf_questions = ionesoft_lemming_tfidf_95(question, tags, answers, questions)
    w2v_tags, w2v_answers, w2v_questions = ionesoft_w2v_100(question, tags, answers, questions)
    return tfidf_tags, tfidf_answers, tfidf_questions, w2v_tags, w2v_answers, w2v_questions


def ionesoft_lemming_90(question, tags, answers, questions):
    tfidf_tags, tfidf_answers, tfidf_questions = ionesoft_lemming_tfidf_90(question, tags, answers, questions)
    w2v_tags, w2v_answers, w2v_questions = ionesoft_w2v_100(question, tags, answers, questions)
    return tfidf_tags, tfidf_answers, tfidf_questions, w2v_tags, w2v_answers, w2v_questions


def ionesoft_stopwords_100(question, tags, answers, questions):
    tfidf_tags, tfidf_answers, tfidf_questions = ionesoft_stopwords_tfidf_100(question, tags, answers, questions)
    w2v_tags, w2v_answers, w2v_questions = ionesoft_w2v_100(question, tags, answers, questions)
    return tfidf_tags, tfidf_answers, tfidf_questions, w2v_tags, w2v_answers, w2v_questions


def ionesoft_stopwords_95(question, tags, answers, questions):
    tfidf_tags, tfidf_answers, tfidf_questions = ionesoft_stopwords_tfidf_95(question, tags, answers, questions)
    w2v_tags, w2v_answers, w2v_questions = ionesoft_w2v_100(question, tags, answers, questions)
    return tfidf_tags, tfidf_answers, tfidf_questions, w2v_tags, w2v_answers, w2v_questions


def ionesoft_stopwords_90(question, tags, answers, questions):
    tfidf_tags, tfidf_answers, tfidf_questions = ionesoft_stopwords_tfidf_90(question, tags, answers, questions)
    w2v_tags, w2v_answers, w2v_questions = ionesoft_w2v_100(question, tags, answers, questions)
    return tfidf_tags, tfidf_answers, tfidf_questions, w2v_tags, w2v_answers, w2v_questions


def ionesoft_stopwords_stemming_100(question, tags, answers, questions):
    tfidf_tags, tfidf_answers, tfidf_questions = ionesoft_stopwords_stemming_tfidf_100(question, tags, answers, questions)
    w2v_tags, w2v_answers, w2v_questions = ionesoft_w2v_100(question, tags, answers, questions)
    return tfidf_tags, tfidf_answers, tfidf_questions, w2v_tags, w2v_answers, w2v_questions


def ionesoft_stopwords_stemming_95(question, tags, answers, questions):
    tfidf_tags, tfidf_answers, tfidf_questions = ionesoft_stopwords_stemming_tfidf_95(question, tags, answers, questions)
    w2v_tags, w2v_answers, w2v_questions = ionesoft_w2v_100(question, tags, answers, questions)
    return tfidf_tags, tfidf_answers, tfidf_questions, w2v_tags, w2v_answers, w2v_questions


def ionesoft_stopwords_stemming_90(question, tags, answers, questions):
    tfidf_tags, tfidf_answers, tfidf_questions = ionesoft_stopwords_stemming_tfidf_90(question, tags, answers, questions)
    w2v_tags, w2v_answers, w2v_questions = ionesoft_w2v_100(question, tags, answers, questions)
    return tfidf_tags, tfidf_answers, tfidf_questions, w2v_tags, w2v_answers, w2v_questions


def ionesoft_stopwords_lemming_100(question, tags, answers, questions):
    tfidf_tags, tfidf_answers, tfidf_questions = ionesoft_stopwords_lemming_tfidf_100(question, tags, answers, questions)
    w2v_tags, w2v_answers, w2v_questions = ionesoft_w2v_100(question, tags, answers, questions)
    return tfidf_tags, tfidf_answers, tfidf_questions, w2v_tags, w2v_answers, w2v_questions


def ionesoft_stopwords_lemming_95(question, tags, answers, questions):
    tfidf_tags, tfidf_answers, tfidf_questions = ionesoft_stopwords_lemming_tfidf_95(question, tags, answers, questions)
    w2v_tags, w2v_answers, w2v_questions = ionesoft_w2v_100(question, tags, answers, questions)
    return tfidf_tags, tfidf_answers, tfidf_questions, w2v_tags, w2v_answers, w2v_questions


def ionesoft_stopwords_lemming_90(question, tags, answers, questions):
    tfidf_tags, tfidf_answers, tfidf_questions = ionesoft_stopwords_lemming_tfidf_90(question, tags, answers, questions)
    w2v_tags, w2v_answers, w2v_questions = ionesoft_w2v_100(question, tags, answers, questions)
    return tfidf_tags, tfidf_answers, tfidf_questions, w2v_tags, w2v_answers, w2v_questions


def stackexchange_tfidf_100(question, tags, answers, questions):
    language_model = load(f'{stack_path}tfidf_100_model.joblib')
    vectorizer = load(f'{stack_path}tfidf_100_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, questions, 10)


def stackexchange_tfidf_95(question, tags, answers, questions):
    language_model = load(f'{stack_path}tfidf_95_model.joblib')
    vectorizer = load(f'{stack_path}tfidf_95_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, questions, 10)


def stackexchange_tfidf_90(question, tags, answers, questions):
    language_model = load(f'{stack_path}tfidf_90_model.joblib')
    vectorizer = load(f'{stack_path}tfidf_90_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, questions, 10)


def stackexchange_stemming_tfidf_100(question, tags, answers, questions):
    language_model = load(f'{stack_path}tfidf_stemming_100_model.joblib')
    vectorizer = load(f'{stack_path}tfidf_stemming_100_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, questions, 10)


def stackexchange_stemming_tfidf_95(question, tags, answers, questions):
    language_model = load(f'{stack_path}tfidf_stemming_95_model.joblib')
    vectorizer = load(f'{stack_path}tfidf_stemming_95_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, questions, 10)


def stackexchange_stemming_tfidf_90(question, tags, answers, questions):
    language_model = load(f'{stack_path}tfidf_stemming_90_model.joblib')
    vectorizer = load(f'{stack_path}tfidf_stemming_90_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, questions, 10)


def stackexchange_lemming_tfidf_100(question, tags, answers, questions):
    language_model = load(f'{stack_path}tfidf_lemming_100_model.joblib')
    vectorizer = load(f'{stack_path}tfidf_lemming_100_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, questions, 10)


def stackexchange_lemming_tfidf_95(question, tags, answers, questions):
    language_model = load(f'{stack_path}tfidf_lemming_95_model.joblib')
    vectorizer = load(f'{stack_path}tfidf_lemming_95_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, questions, 10)


def stackexchange_lemming_tfidf_90(question, tags, answers, questions):
    language_model = load(f'{stack_path}tfidf_lemming_90_model.joblib')
    vectorizer = load(f'{stack_path}tfidf_lemming_90_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, questions, 10)


def stackexchange_stopwords_tfidf_100(question, tags, answers, questions):
    language_model = load(f'{stack_path}tfidf_stopwords_100_model.joblib')
    vectorizer = load(f'{stack_path}tfidf_stopwords_100_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, questions, 10)


def stackexchange_stopwords_tfidf_95(question, tags, answers, questions):
    language_model = load(f'{stack_path}tfidf_stopwords_95_model.joblib')
    vectorizer = load(f'{stack_path}tfidf_stopwords_95_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, questions, 10)


def stackexchange_stopwords_tfidf_90(question, tags, answers, questions):
    language_model = load(f'{stack_path}tfidf_stopwords_90_model.joblib')
    vectorizer = load(f'{stack_path}tfidf_stopwords_90_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, questions, 10)


def stackexchange_stopwords_stemming_tfidf_100(question, tags, answers, questions):
    language_model = load(f'{stack_path}tfidf_stopwords_stemming_100_model.joblib')
    vectorizer = load(f'{stack_path}tfidf_stopwords_stemming_100_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, questions, 10)


def stackexchange_stopwords_stemming_tfidf_95(question, tags, answers, questions):
    language_model = load(f'{stack_path}tfidf_stopwords_stemming_95_model.joblib')
    vectorizer = load(f'{stack_path}tfidf_stopwords_stemming_95_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, questions, 10)


def stackexchange_stopwords_stemming_tfidf_90(question, tags, answers, questions):
    language_model = load(f'{stack_path}tfidf_stopwords_stemming_90_model.joblib')
    vectorizer = load(f'{stack_path}tfidf_stopwords_stemming_90_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, questions, 10)


def stackexchange_stopwords_lemming_tfidf_100(question, tags, answers, questions):
    language_model = load(f'{stack_path}tfidf_stopwords_lemming_100_model.joblib')
    vectorizer = load(f'{stack_path}tfidf_stopwords_lemming_100_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, questions, 10)


def stackexchange_stopwords_lemming_tfidf_95(question, tags, answers, questions):
    language_model = load(f'{stack_path}tfidf_stopwords_lemming_95_model.joblib')
    vectorizer = load(f'{stack_path}tfidf_stopwords_lemming_95_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, questions, 10)


def stackexchange_stopwords_lemming_tfidf_90(question, tags, answers, questions):
    language_model = load(f'{stack_path}tfidf_stopwords_lemming_90_model.joblib')
    vectorizer = load(f'{stack_path}tfidf_stopwords_lemming_90_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, questions, 10)


def stackexchange_w2v_100(question, tags, answers, questions):
    model = Word2Vec.load(f'{stack_path}w2v_100_model.w2v')
    question_vectors = pickle.load(open(f'{stack_path}w2v_100_vectors.pickle', 'rb'))
    return predict_n_w2v_answers(question, model, question_vectors, tags, answers, questions, 10)


ione_path = 'models/ionesoft/'


def ionesoft_tfidf_100(question, tags, answers, questions):
    language_model = load(f'{ione_path}tfidf_100_model.joblib')
    vectorizer = load(f'{ione_path}tfidf_100_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, questions, 10)


def ionesoft_tfidf_95(question, tags, answers, questions):
    language_model = load(f'{ione_path}tfidf_95_model.joblib')
    vectorizer = load(f'{ione_path}tfidf_95_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, questions, 10)


def ionesoft_tfidf_90(question, tags, answers, questions):
    language_model = load(f'{ione_path}tfidf_90_model.joblib')
    vectorizer = load(f'{ione_path}tfidf_90_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, questions, 10)


def ionesoft_stemming_tfidf_100(question, tags, answers, questions):
    language_model = load(f'{ione_path}tfidf_stemming_100_model.joblib')
    vectorizer = load(f'{ione_path}tfidf_stemming_100_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, questions, 10)


def ionesoft_stemming_tfidf_95(question, tags, answers, questions):
    language_model = load(f'{ione_path}tfidf_stemming_95_model.joblib')
    vectorizer = load(f'{ione_path}tfidf_stemming_95_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, questions, 10)


def ionesoft_stemming_tfidf_90(question, tags, answers, questions):
    language_model = load(f'{ione_path}tfidf_stemming_90_model.joblib')
    vectorizer = load(f'{ione_path}tfidf_stemming_90_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, questions, 10)


def ionesoft_lemming_tfidf_100(question, tags, answers, questions):
    language_model = load(f'{ione_path}tfidf_lemming_100_model.joblib')
    vectorizer = load(f'{ione_path}tfidf_lemming_100_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, questions, 10)


def ionesoft_lemming_tfidf_95(question, tags, answers, questions):
    language_model = load(f'{ione_path}tfidf_lemming_95_model.joblib')
    vectorizer = load(f'{ione_path}tfidf_lemming_95_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, questions, 10)


def ionesoft_lemming_tfidf_90(question, tags, answers, questions):
    language_model = load(f'{ione_path}tfidf_lemming_90_model.joblib')
    vectorizer = load(f'{ione_path}tfidf_lemming_90_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, questions, 10)


def ionesoft_stopwords_tfidf_100(question, tags, answers, questions):
    language_model = load(f'{ione_path}tfidf_stopwords_100_model.joblib')
    vectorizer = load(f'{ione_path}tfidf_stopwords_100_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, questions, 10)


def ionesoft_stopwords_tfidf_95(question, tags, answers, questions):
    language_model = load(f'{ione_path}tfidf_stopwords_95_model.joblib')
    vectorizer = load(f'{ione_path}tfidf_stopwords_95_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, questions, 10)


def ionesoft_stopwords_tfidf_90(question, tags, answers, questions):
    language_model = load(f'{ione_path}tfidf_stopwords_90_model.joblib')
    vectorizer = load(f'{ione_path}tfidf_stopwords_90_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, questions, 10)


def ionesoft_stopwords_stemming_tfidf_100(question, tags, answers, questions):
    language_model = load(f'{ione_path}tfidf_stopwords_stemming_100_model.joblib')
    vectorizer = load(f'{ione_path}tfidf_stopwords_stemming_100_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, questions, 10)


def ionesoft_stopwords_stemming_tfidf_95(question, tags, answers, questions):
    language_model = load(f'{ione_path}tfidf_stopwords_stemming_95_model.joblib')
    vectorizer = load(f'{ione_path}tfidf_stopwords_stemming_95_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, questions, 10)


def ionesoft_stopwords_stemming_tfidf_90(question, tags, answers, questions):
    language_model = load(f'{ione_path}tfidf_stopwords_stemming_90_model.joblib')
    vectorizer = load(f'{ione_path}tfidf_stopwords_stemming_90_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, questions, 10)


def ionesoft_stopwords_lemming_tfidf_100(question, tags, answers, questions):
    language_model = load(f'{ione_path}tfidf_stopwords_lemming_100_model.joblib')
    vectorizer = load(f'{ione_path}tfidf_stopwords_lemming_100_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, questions, 10)


def ionesoft_stopwords_lemming_tfidf_95(question, tags, answers, questions):
    language_model = load(f'{ione_path}tfidf_stopwords_lemming_95_model.joblib')
    vectorizer = load(f'{ione_path}tfidf_stopwords_lemming_95_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, questions, 10)


def ionesoft_stopwords_lemming_tfidf_90(question, tags, answers, questions):
    language_model = load(f'{ione_path}tfidf_stopwords_lemming_90_model.joblib')
    vectorizer = load(f'{ione_path}tfidf_stopwords_lemming_90_vectorizer.joblib')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, questions, 10)


def ionesoft_w2v_100(question, tags, answers, questions):
    model = Word2Vec.load(f'{ione_path}w2v_100_model.w2v')
    question_vectors = pickle.load(open(f'{ione_path}w2v_100_vectors.pickle', 'rb'))
    return predict_n_w2v_answers(question, model, question_vectors, tags, answers, questions, 10)
