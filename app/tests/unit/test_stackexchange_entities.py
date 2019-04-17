from bda_core.entities.stackexchange.utils import (
    strip_html,
    remove_newline,
    is_question,
    extract_text_with_id,
    extract_answer_id,
    save_as_json
)

row = {
    'Id': '1',
    'AcceptedAnswerId': '925',
    'Body': '&lt;p&gt;My chocolate chips cookies are always too crisp. How can I get chewy cookies, like those of Starbucks?&lt;/p&gt;&#xA;&#xA;&lt;hr&gt;&#xA;&#xA;&lt;p&gt;Thank you to everyone who has answered.\n So far the tip that had the biggest impact was to chill and rest the dough, however I also increased the brown sugar ratio and increased a bit the butter. Also adding maple syrup helped. &lt;/p&gt;&#xA;'
}

def test_stip_html():
    assert strip_html(row['Body']) == 'pMy chocolate chips cookies are always too crisp. How can I get chewy cookies, like those of Starbucks?/phrpThank you to everyone who has answered.\n So far the tip that had the biggest impact was to chill and rest the dough, however I also increased the brown sugar ratio and increased a bit the butter. Also adding maple syrup helped. /p'

def test_remove_newline():
    assert remove_newline(row['Body']) == '&lt;p&gt;My chocolate chips cookies are always too crisp. How can I get chewy cookies, like those of Starbucks?&lt;/p&gt;&#xA;&#xA;&lt;hr&gt;&#xA;&#xA;&lt;p&gt;Thank you to everyone who has answered.  So far the tip that had the biggest impact was to chill and rest the dough, however I also increased the brown sugar ratio and increased a bit the butter. Also adding maple syrup helped. &lt;/p&gt;&#xA;'

def test_is_question_should_be_true():
    assert is_question(row) == True

def test_is_question_should_be_false():
    answer_row = {
        'AcceptedAnswerId': None
    }
    assert is_question(answer_row) == False

def test_extract_text_with_id():
    text, id = extract_text_with_id(row)
    assert text == 'pMy chocolate chips cookies are always too crisp. How can I get chewy cookies, like those of Starbucks?/phrpThank you to everyone who has answered.  So far the tip that had the biggest impact was to chill and rest the dough, however I also increased the brown sugar ratio and increased a bit the butter. Also adding maple syrup helped. /p'
    assert id == 1

def test_extract_answer_id():
    assert extract_answer_id(row) == 925

def test_save_as_json():
    store = {'questions_answers': []}
    question = 'when was I born?'
    answer_id = 42
    answer = '1993'
    save_as_json(question, answer_id, answer, store)
    assert store['questions_answers'] == [
        {
            'answer_id': answer_id,
            'question': question,
            'answer': answer
        }
    ]
