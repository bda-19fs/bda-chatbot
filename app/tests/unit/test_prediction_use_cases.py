from bda_core.use_cases.prediction.algorithm import (
    algorithm_strategy,
    stackexchange_100,
    stackexchange_95,
    stackexchange_90
)
from bda_core.use_cases.prediction.utils import (
    readable,
    readable_w2v
)


def test_readable():
    answers = ['1993']
    probs = [(0, [1.0])]
    assert readable(probs, answers) == ['1.0, 1993']

def test_readable_w2v():
    answers = ['1993']
    probs = [(0, [[1.0]])]
    assert readable_w2v(probs, answers) == ['1.0, 1993']

def test_algorithm_strategy_100():
    config_tfidf = {
        'dataset': 0,
        'algorithm': 0,
        'domain_limit': 0
    }
    algorithm = algorithm_strategy(config_tfidf)
    assert algorithm is stackexchange_100

def test_algorithm_strategy_95():
    config_tfidf = {
        'dataset': 0,
        'algorithm': 0,
        'domain_limit': 1
    }
    algorithm = algorithm_strategy(config_tfidf)
    assert algorithm is stackexchange_95

def test_algorithm_strategy_90():
    config_tfidf = {
        'dataset': 0,
        'algorithm': 0,
        'domain_limit': 2
    }
    algorithm = algorithm_strategy(config_tfidf)
    assert algorithm is stackexchange_90
