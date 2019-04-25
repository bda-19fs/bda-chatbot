from bda_core.use_cases.prediction.algorithm import (
    algorithm_strategy,
    stackexchange_tfidf_100
)
from bda_core.use_cases.prediction.utils import (
    readable
)


config_tfidf = {
    'dataset': 0,
    'algorithm': 0,
    'domain_limit': 0
}

def test_readable():
    answers = ['1993']
    probs = [(0, [1.0])]
    assert readable(probs, answers) == ['1.0, 1993']

def test_algorithm_strategy():
    algorithm = algorithm_strategy(config_tfidf)
    assert algorithm is stackexchange_tfidf_100
