#!/usr/bin/env python3
import click
import untangle
import time as watch
from bda_core.use_cases.log.log_info import log_info
from bda_core.use_cases.stackexchange.extract_questions_with_answers import (
    extract_questions_with_answers
)


def save(extract, questions_file, answers_file, tags_file):
    with open(questions_file, 'w', encoding='utf-8') as q_file:
        with open(answers_file, 'w', encoding='utf-8') as a_file:
            with open(tags_file, 'w', encoding='utf-8') as t_file:
                for element in extract['questions_answers']:
                    q = element['question']
                    a = element['answer']
                    t = element['tags']
                    if q and a:
                        q = q.replace(',', '')
                        a = a.replace(',', '')
                        q_file.write(f'{q}\n')
                        a_file.write(f'{a}\n')
                        t_file.write(f'{t}\n')


@click.command()
@click.option(
    '-x', '--xml_file', type=click.STRING, default='data/posts.xml',
    help='choose stackexchange xml file (default is "data/posts.xml")'
)
@click.option(
    '-q', '--questions_file', type=click.STRING, default='stackexchange_questions.txt',
    help='choose output file name (default is "stackexchange_questions.txt")'
)
@click.option(
    '-a', '--answers_file', type=click.STRING, default='stackexchange_answers.txt',
    help='choose output file name (default is "stackexchange_answers.txt")'
)
@click.option(
    '-t', '--tags_file', type=click.STRING, default='stackexchange_tags.txt',
    help='choose output file name (default is "stackexchange_tags.txt")'
)
def stackexchange(xml_file, questions_file, answers_file, tags_file):
    start = watch.time()

    log_info(f'extract questions with answers from stackexchange')

    xml = untangle.parse(xml_file)
    extract = extract_questions_with_answers(xml)

    save(extract, questions_file, answers_file, tags_file)

    log_info(f'extraction completed in {watch.time() - start}s\n')


if __name__ == '__main__':
    stackexchange()
