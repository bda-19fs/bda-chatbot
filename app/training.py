#!/usr/bin/env python3
import os
import json
import click
import time as watch
from joblib import dump
from bda_core.use_cases.log.log_info import log_info
from bda_core.use_cases.training.model import create_language_model
from bda_core.entities.file.json_handler import from_str_to_json


def get_concepts_from_folder(wiki_extracts):
    concepts = []
    for extract in os.listdir(wiki_extracts):
        if extract.startswith('wiki_'):
            log_info(f'- collecting {extract}')
            with open(wiki_extracts + extract, 'r', encoding='utf-8') as f:
                for line in f.readlines():
                    json_concept = from_str_to_json(line)
                    concepts.append(json_concept['text'])
    return concepts

def file_as_list(file):
    with open(file, 'r', encoding='utf-8') as file:
        return list(map(lambda line: line.strip(), file.readlines()))

def save(model, vectorizer, model_name, vec_name):
    dump(model, f'{model_name}.joblib')
    dump(vectorizer, f'{vec_name}.joblib')

@click.command()
@click.option(
    '-w', '--wiki_extracts', type=click.STRING, required=True,
    help='choose wiki extract folder'
)
@click.option(
    '-q', '--questions', type=click.STRING, required=True,
    help='choose questions file'
)
def training(wiki_extracts, questions):
    start = watch.time()

    log_info(f'collecting wiki_extracts from folder {wiki_extracts}')
    concepts = get_concepts_from_folder(wiki_extracts)
    log_info(f'found {len(concepts)} concepts')

    questions = file_as_list(questions)
    log_info(f'collected {len(questions)} questions')

    log_info(f'creating language model')
    model_100, vectorizer_100 = create_language_model(concepts, questions, 0)
    model_95, vectorizer_95 = create_language_model(concepts, questions, 0.05)
    model_90, vectorizer_90 = create_language_model(concepts, questions, 0.1)

    save(model_100, vectorizer_100, 'tfidf_100_model', 'tfidf_100_vectorizer')
    save(model_95, vectorizer_95, 'tfidf_95_model', 'tfidf_95_vectorizer')
    save(model_90, vectorizer_90, 'tfidf_90_model', 'tfidf_90_vectorizer')

    log_info(f'training completed in {watch.time() - start}s\n')


if __name__ == '__main__':
    training()
