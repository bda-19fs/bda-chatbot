from joblib import load
from bda_core.use_cases.prediction.utils import predict_n_answers


def file_as_list(file):
    with open(file, 'r', encoding='utf-8') as file:
        return list(map(lambda line: line.strip(), file.readlines()))

def handle_request(question):
    language_model = load('models/language_model.joblib')
    vectorizer = load('models/language_model_vectorizer.joblib')
    answers = file_as_list('models/stackexchange_tags.txt')
    return predict_n_answers(language_model, vectorizer, [question], answers, 10)
