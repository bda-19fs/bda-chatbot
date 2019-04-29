from bda_core.entities.file.json_handler import (
    from_str_to_json,
    dump_json
)

from bda_core.entities.file.reader import (
    file_as_list,
    file_as_dict
)


json_as_str = '["foo", {"bar": ["baz", null, 1.0, 2]}]'
json = [u'foo', {u'bar': [u'baz', None, 1.0, 2]}]

def test_from_str_to_json():
    assert from_str_to_json(json_as_str) == json

def test_dump_json():
    assert dump_json(json) == json_as_str

CONTENT = '''category1;answer1
category2;answer2
category3;answer3
'''

def test_file_as_list(tmp_path):
    words_test = tmp_path / 'test.csv'
    words_test.write_text(CONTENT)
    words = file_as_list(words_test, local=False)
    assert words == [
        'category1;answer1',
        'category2;answer2',
        'category3;answer3'
    ]

def test_file_as_dict(tmp_path):
    words_test = tmp_path / 'test.csv'
    words_test.write_text(CONTENT)
    words = file_as_dict(words_test, sep=';', local=False)
    assert words == {
        'category1': 'answer1',
        'category2': 'answer2',
        'category3': 'answer3'
    }
