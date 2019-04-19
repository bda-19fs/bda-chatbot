import json


def from_str_to_json(line):
    '''
    Converts the given json string to a python dict.
    :param line: The input json string
    :return: A python dict
    '''
    return json.loads(line, encoding='utf8')


def dump_json(json_doc):
    '''
    Converts the given json document (dict) to a json string
    :param json_doc: The input dict
    :return: A json string
    '''
    return json.dumps(json_doc)
