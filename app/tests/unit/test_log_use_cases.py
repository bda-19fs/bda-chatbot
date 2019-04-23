import logging
from bda_core.use_cases.log.log_info import log_info


def test_log_info(capsys):
    logging.getLogger().addHandler(logging.StreamHandler())
    log_info(msg='I am in a unit test', log=logging)
    captured = capsys.readouterr()
    log_msg = 'I am in a unit test\n'
    assert captured.err == log_msg
