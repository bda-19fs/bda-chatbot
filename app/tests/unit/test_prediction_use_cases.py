from bda_core.use_cases.prediction.utils import (
    readable,
    predict_closest
)


def test_readable():
    answers = ['1993']
    probs = [(0, [1.0])]
    assert readable(probs, answers) == ['1.0, 1993']
