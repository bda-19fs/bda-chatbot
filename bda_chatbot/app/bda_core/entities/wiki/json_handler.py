import json


def from_str_to_json(line):
    return json.loads(line, encoding='utf8')


def dump_json(json_doc):
    return json.dumps(json_doc)
