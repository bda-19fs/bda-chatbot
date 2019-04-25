from joblib import load
from bda_core.use_cases.prediction.utils import predict_n_answers


def file_as_list(file):
    with open(file, 'r', encoding='utf-8') as file:
        return list(map(lambda line: line.strip(), file.readlines()))

def algorithm_strategy(config):
    config = f'{config["dataset"]}{config["algorithm"]}{config["domain_limit"]}'
    strategy = {
        '000': stackexchange_tfidf_100
    }
    return strategy.get(config, 'unknown config')

stack_path = 'models/stackexchange/'
def stackexchange_tfidf_100(question):
    language_model = load(f'{stack_path}tfidf_100_model.joblib')
    vectorizer = load(f'{stack_path}tfidf_100_vectorizer.joblib')
    tags = file_as_list(f'{stack_path}stackexchange_tags.txt')
    answers = file_as_list(f'{stack_path}stackexchange_answers.txt')
    return predict_n_answers(language_model, vectorizer, [question], tags, answers, 10)
