from bda_core.entities.wiki.json_handler import (
    from_str_to_json,
    dump_json
)

json_as_str = '["foo", {"bar": ["baz", null, 1.0, 2]}]'
json = [u'foo', {u'bar': [u'baz', None, 1.0, 2]}]

def test_from_str_to_json():
    assert from_str_to_json(json_as_str) == json

def test_dump_json():
    assert dump_json(json) == json_as_str
