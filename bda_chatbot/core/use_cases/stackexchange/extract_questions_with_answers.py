import json
from entities.stackexchange.utils import is_question, update_answer_or_save, update_question_or_save


def extract_questions_with_answers(xml, save_file):
    store = {'questions_answers': []}
    question, answer = None, None
    answer_ids = []


    for row in xml.posts.row:
        if is_question(row):
            update_answer_or_save(row, answer_ids, store)
        else:
            update_question_or_save(row, answer_ids, store)

    with open(save_file, 'w', encoding='utf-8') as f:
        json.dump(store, f, indent=2)


if __name__ == '__main__':
    extract_questions_with_answers()
