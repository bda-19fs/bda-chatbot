#!/usr/bin/env python3
import os
import click
import pickle
import time as watch
from bda_core.use_cases.log.log_info import log_info
from bda_core.use_cases.training.model import create_w2v_model
from bda_core.entities.file.json_handler import from_str_to_json


def get_concepts_from_folder(wiki_extracts):
    concepts = []
    for extract in os.listdir(wiki_extracts):
        if extract.startswith('wiki_'):
            log_info(f'- collecting {extract}')
            with open(wiki_extracts + extract, 'r', encoding='utf-8') as f:
                for line in f.readlines():
                    json_concept = from_str_to_json(line)
                    sentences_list = json_concept['text'].split()
                    concepts.append(sentences_list)
    return concepts


def file_as_list(file):
    with open(file, 'r', encoding='utf-8') as file:
        return list(map(lambda line: line.strip().lower().split(), file.readlines()))


def save_model(model, file_name):
    model.save(file_name)


def save_pre_computed_vectors(vectors, file_name):
    pickle.dump(vectors, open(file_name, 'wb'))


@click.command()
@click.option(
    '-w', '--wiki_extracts', type=click.STRING, required=True,
    help='choose wiki extract folder'
)
@click.option(
    '-q', '--questions', type=click.STRING, required=True,
    help='choose questions file'
)
@click.option(
    '-f', '--file_name', type=click.STRING, default='w2v_model',
    help='choose name for language model. default("w2v_model")'
)
def training(wiki_extracts, questions, file_name):
    start = watch.time()

    log_info(f'collecting wiki_extracts from folder {wiki_extracts}')
    concepts = get_concepts_from_folder(wiki_extracts)
    log_info(f'found {len(concepts)} concepts')

    questions = file_as_list(questions)
    log_info(f'collected {len(questions)} questions')

    log_info(f'creating language model')
    model, vectors = create_w2v_model(concepts, questions)

    save_model(model, file_name)
    save_pre_computed_vectors(vectors, file_name + '_vectors')

    log_info(f'training completed in {watch.time() - start}s\n')


if __name__ == '__main__':
    training()
