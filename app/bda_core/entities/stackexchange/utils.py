import re


def strip_html(text):
    return re.sub('&[^;]+;|<[^>]+>', '', text)

def remove_newline(text):
    text = text.replace('\n', ' ')
    return re.sub('\s\s+', ' ', text)

def is_question(row):
    return True if extract_answer_id(row) else False

def extract_text_with_id(row):
    id = int(row['Id'])
    text = strip_html(row['Body'])
    text = remove_newline(text)
    return text, id

def extract_answer_id(row):
    answer_id = row['AcceptedAnswerId']
    return int(answer_id) if answer_id else None

def save_as_json(question, answer_id, answer, store):
    store['questions_answers'].append(
        {
            'answer_id': answer_id,
            'question': question,
            'answer': answer
        })

def update_answer_or_save(row, answer_ids, store):
    question, question_id = extract_text_with_id(row)
    answer_id = extract_answer_id(row)
    if answer_id in answer_ids:
        obj = next(qa for qa in store['questions_answers'] if qa['answer_id'] == answer_id)
        obj['question'] = question
    else:
        answer_ids.append(answer_id)
        save_as_json(question, answer_id, None, store)

def update_question_or_save(row, answer_ids, store):
    answer, answer_id = extract_text_with_id(row)
    if answer_id in answer_ids:
        obj = next(qa for qa in store['questions_answers'] if qa['answer_id'] == answer_id)
        obj['answer'] = answer
    else:
        answer_ids.append(answer_id)
        save_as_json(None, answer_id, answer, store)
