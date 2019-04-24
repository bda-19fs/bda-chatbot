from joblib import load
from bda_core.use_cases.prediction.utils import predict_n_answers
# from gensim.models import Word2Vec
# import pickle

def file_as_list(file):
    with open(file, 'r', encoding='utf-8') as file:
        return list(map(lambda line: line.strip(), file.readlines()))

def handle_request(question):
    language_model = load('models/language_model.joblib')
    vectorizer = load('models/language_model_vectorizer.joblib')
    answers = file_as_list('models/stackexchange_tags.txt')
    return predict_n_answers(language_model, vectorizer, [question], answers, 10)


# model = Word2Vec.load('filename')
# question_vectors = pickle.load(open('filename_vectors', 'rb'))
# predict_n_w2v_answers(model, question_vectors, answers, 10)
