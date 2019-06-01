import re
import pickle

from gensim.models import Word2Vec
from joblib import load

from bda_core.entities.file.reader import file_as_list


stack = '/mnt/data/models/stackexchange/'
ione = '/mnt/data/models/ionesoft/'
def get_model_components(config):
    config = f'{config["dataset"]}{config["algorithm"]}{config["domain_limit"]}'
    strategy = {
        '000': (stack, '_100_model', '_100_vectors'),
        '001': (stack, '_75_model', '_75_vectors'),
        '002': (stack, '_50_model', '_50_vectors'),
        '010': (stack, '_stemming_100_model', '_stemming_100_vectors'),
        '011': (stack, '_stemming_75_model', '_stemming_75_vectors'),
        '012': (stack, '_stemming_50_model', '_stemming_50_vectors'),
        '020': (stack, '_lemming_100_model', '_lemming_100_vectors'),
        '021': (stack, '_lemming_75_model', '_lemming_75_vectors'),
        '022': (stack, '_lemming_50_model', '_lemming_50_vectors'),
        '030': (stack, '_stopwords_100_model', '_stopwords_100_vectors'),
        '031': (stack, '_stopwords_75_model', '_stopwords_75_vectors'),
        '032': (stack, '_stopwords_50_model', '_stopwords_50_vectors'),
        '040': (stack, '_stopwords_stemming_100_model', '_stopwords_stemming_100_vectors'),
        '041': (stack, '_stopwords_stemming_75_model', '_stopwords_stemming_75_vectors'),
        '042': (stack, '_stopwords_stemming_50_model', '_stopwords_stemming_50_vectors'),
        '050': (stack, '_stopwords_lemming_100_model', '_stopwords_lemming_100_vectors'),
        '051': (stack, '_stopwords_lemming_75_model', '_stopwords_lemming_75_vectors'),
        '052': (stack, '_stopwords_lemming_50_model', '_stopwords_lemming_50_vectors'),
        '100': (ione, '_100_model', '_100_vectors'),
        '101': (ione, '_75_model', '_75_vectors'),
        '102': (ione, '_50_model', '_50_vectors'),
        '110': (ione, '_stemming_100_model', '_stemming_100_vectors'),
        '111': (ione, '_stemming_75_model', '_stemming_75_vectors'),
        '112': (ione, '_stemming_50_model', '_stemming_50_vectors'),
        '120': (ione, '_lemming_100_model', '_lemming_100_vectors'),
        '121': (ione, '_lemming_75_model', '_lemming_75_vectors'),
        '122': (ione, '_lemming_50_model', '_lemming_50_vectors'),
        '130': (ione, '_stopwords_100_model', '_stopwords_100_vectors'),
        '131': (ione, '_stopwords_75_model', '_stopwords_75_vectors'),
        '132': (ione, '_stopwords_50_model', '_stopwords_50_vectors'),
        '140': (ione, '_stopwords_stemming_100_model', '_stopwords_stemming_100_vectors'),
        '141': (ione, '_stopwords_stemming_75_model', '_stopwords_stemming_75_vectors'),
        '142': (ione, '_stopwords_stemming_50_model', '_stopwords_stemming_50_vectors'),
        '150': (ione, '_stopwords_lemming_100_model', '_stopwords_lemming_100_vectors'),
        '151': (ione, '_stopwords_lemming_75_model', '_stopwords_lemming_75_vectors'),
        '152': (ione, '_stopwords_lemming_50_model', '_stopwords_lemming_50_vectors')
    }
    strategy = strategy.get(config, 'unknown config')
    return strategy[0], strategy[1], strategy[2]


def load_models(folder, model, vectors):
    language_model_tfidf = load(f'{folder}tfidf{model}.joblib')
    vectors_tfidf = load(f'{folder}tfidf{vectors}.joblib')
    # fix because there are currently only 100 w2v models
    model_w2v = re.sub('_\d{2}_', '_100_', model)
    vectors_w2v = re.sub('_\d{2}_', '_100_', vectors)
    language_model_w2v = load(f'{folder}w2v{model_w2v}.w2v')
    vectors_w2v = load(f'{folder}w2v{vectors_w2v}.pickle')
    return language_model_tfidf, vectors_tfidf, language_model_w2v, vectors_w2v


def load_tags_answers(dataset):
    tags = file_as_list(f'/mnt/data/raw/{dataset}_tags.txt', local=False)
    answers = file_as_list(f'/mnt/data/raw/{dataset}_answers.txt', local=False)
    questions = file_as_list(f'/mnt/data/raw/{dataset}_questions.txt', local=False)
    return tags, answers, questions


def load_vocab_match(vocab, question):
    question = question.split(' ')
    question = filter(lambda x: x in vocab, question)
    return str.join(' ', question)
