#!/usr/bin/env python3
import click
import untangle
import time as watch
from bda_core.use_cases.log.log_info import log_info
from bda_core.use_cases.stackexchange.extract_questions_with_answers import (
    extract_questions_with_answers
)


@click.command()
@click.option(
    '-x', '--xml_file', type=click.STRING, default='data/posts.xml',
    help='choose stackexchange xml file (default is "data/posts.xml")'
)
@click.option(
    '-s', '--save_file', type=click.STRING, default='stackexchange_questions_answers.txt',
    help='choose output file name (default is "stackexchange_questions_answers.txt")'
)
def stackexchange(xml_file, save_file):
    start = watch.time()

    log_info(f'extract questions with answers from stackexchange')

    xml = untangle.parse(xml_file)
    extract = extract_questions_with_answers(xml)

    with open(save_file, 'w', encoding='utf-8') as f:
        for element in extract['questions_answers']:
            q = element['question']
            a = element['answer']
            if q and a:
                q = q.replace(',', '')
                a = a.replace(',', '')
                f.write(f'{q},{a}\n')

    log_info(f'extraction completed in {watch.time() - start}s\n')


if __name__ == '__main__':
    stackexchange()
