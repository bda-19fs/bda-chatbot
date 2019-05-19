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
    probs = [(0, [1.0])]
    assert readable_w2v(probs, answers) == ['1.0, 1993']
