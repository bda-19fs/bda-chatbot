import json


def from_str_to_json(line):
    return json.loads(line, encoding='utf8')
