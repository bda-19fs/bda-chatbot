from bda_core.entities.stackexchange.utils import (
    strip_html,
    remove_newline,
    is_question,
    extract_tags,
    extract_text_with_id,
    extract_answer_id,
    save_as_json,
    update_answer_or_save,
    update_question_or_save
)

row = {
    'Id': '1',
    'AcceptedAnswerId': '925',
    'Body': '&lt;p&gt;My chocolate chips cookies are always too crisp. How can I get chewy cookies, like those of Starbucks?&lt;/p&gt;&#xA;&#xA;&lt;hr&gt;&#xA;&#xA;&lt;p&gt;Thank you to everyone who has answered.\n So far the tip that had the biggest impact was to chill and rest the dough, however I also increased the brown sugar ratio and increased a bit the butter. Also adding maple syrup helped. &lt;/p&gt;&#xA;',
    'Tags': '&lt;test&gt;'
}

row_two = {
    'Id': '2',
    'AcceptedAnswerId': '123',
    'Body': 'How old am I?',
    'Tags': '&lt;test&gt;&lt;testing&gt;'
}

row_answer = {
    'Id': '123',
    'AcceptedAnswerId': None,
    'Body': '1993'
}

def test_stip_html():
    assert strip_html(row['Body']) == 'pMy chocolate chips cookies are always too crisp. How can I get chewy cookies, like those of Starbucks?/phrpThank you to everyone who has answered.\n So far the tip that had the biggest impact was to chill and rest the dough, however I also increased the brown sugar ratio and increased a bit the butter. Also adding maple syrup helped. /p'

def test_remove_newline():
    assert remove_newline(row['Body']) == '&lt;p&gt;My chocolate chips cookies are always too crisp. How can I get chewy cookies, like those of Starbucks?&lt;/p&gt;&#xA;&#xA;&lt;hr&gt;&#xA;&#xA;&lt;p&gt;Thank you to everyone who has answered. So far the tip that had the biggest impact was to chill and rest the dough, however I also increased the brown sugar ratio and increased a bit the butter. Also adding maple syrup helped. &lt;/p&gt;&#xA;'

def test_is_question_should_be_true():
    assert is_question(row) == True

def test_is_question_should_be_false():
    answer_row = {
        'AcceptedAnswerId': None
    }
    assert is_question(answer_row) == False

def test_extract_tags():
    assert extract_tags(row) == '&lt;test&gt;'

def test_extract_text_with_id():
    text, id = extract_text_with_id(row)
    assert text == 'pMy chocolate chips cookies are always too crisp. How can I get chewy cookies, like those of Starbucks?/phrpThank you to everyone who has answered. So far the tip that had the biggest impact was to chill and rest the dough, however I also increased the brown sugar ratio and increased a bit the butter. Also adding maple syrup helped. /p'
    assert id == 1

def test_extract_answer_id():
    assert extract_answer_id(row) == 925

def test_save_as_json():
    store = {'questions_answers': []}
    question = 'when was I born?'
    answer_id = 42
    answer = '1993'
    tags = 'test testing'
    save_as_json(question, answer_id, answer, tags, store)
    assert store['questions_answers'] == [
        {
            'answer_id': answer_id,
            'question': question,
            'answer': answer,
            'tags': 'test testing'
        }
    ]

def test_update_answer_or_save_should_update_answer():
    store = {'questions_answers': [
        {
            'answer_id': 123,
            'question': None,
            'answer': '1993'
        }
    ]}
    answer_ids = [123]
    update_answer_or_save(row_two, answer_ids, store)
    assert store['questions_answers'] == [
        {
            'answer_id': 123,
            'question': 'How old am I?',
            'answer': '1993',
            'tags': '&lt;test&gt;&lt;testing&gt;'
        }
    ]

def test_update_answer_or_save_should_save():
    store = {'questions_answers': []}
    answer_ids = []
    update_answer_or_save(row_two, answer_ids, store)
    assert store['questions_answers'] == [
        {
            'answer_id': 123,
            'question': 'How old am I?',
            'answer': None,
            'tags': '&lt;test&gt;&lt;testing&gt;'
        }
    ]

def test_update_question_or_save_should_update():
    store = {'questions_answers': [
        {
            'answer_id': 123,
            'question': 'How old am I?',
            'answer': None
        }
    ]}
    answer_ids = [123]
    update_question_or_save(row_answer, answer_ids, store)
    assert store['questions_answers'] == [
        {
            'answer_id': 123,
            'question': 'How old am I?',
            'answer': '1993'
        }
    ]

def test_update_question_or_save_should_save():
    store = {'questions_answers': []}
    answer_ids = []
    update_question_or_save(row_answer, answer_ids, store)
    assert store['questions_answers'] == [
        {
            'answer_id': 123,
            'question': None,
            'answer': '1993',
            'tags': None
        }
    ]
