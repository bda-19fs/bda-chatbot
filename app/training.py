#!/usr/bin/env python3
import os

import click
import time as watch
from joblib import dump
from bda_core.entities.file.json_handler import from_str_to_json
from bda_core.entities.file.reader import file_as_list
from bda_core.use_cases.log.log_info import log_info
from bda_core.use_cases.nlp.normalize_doc import normalize_doc_stream
from bda_core.use_cases.nlp.correct_grammar import correct_grammar_stream
from bda_core.use_cases.nlp.remove_stopwords import remove_stopwords_stream
from bda_core.use_cases.nlp.stemm_doc import stemm_doc_stream
from bda_core.use_cases.nlp.lemm_doc import lemm_doc_stream
from bda_core.use_cases.training.model import create_language_model


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


def save(model, vectorizer, model_name, vec_name):
    dump(model, f'{model_name}.joblib')
    dump(vectorizer, f'{vec_name}.joblib')


@click.group(chain=True, invoke_without_command=True)
@click.option(
    '-w', '--wiki_extracts', type=click.STRING, required=True,
    help='choose wiki extract folder'
)
@click.option(
    '-q', '--questions', type=click.STRING, required=True,
    help='choose questions file'
)
def cli(wiki_extracts, questions):
    pass


@cli.resultcallback()
def process_pipeline(processors, wiki_extracts, questions):
    start = watch.time()
    concepts = get_concepts_from_folder(wiki_extracts)
    questions = (line.rstrip('\r\n') for line in file_as_list(questions, local=False))
    for processor in processors:
        questions = processor(questions)
        concepts = processor(concepts)
    concepts = list(concepts)
    questions = list(questions)
    log_info(f'creating language model')
    model_100, vectorizer_100 = create_language_model(concepts, questions, 0)
    model_95, vectorizer_95 = create_language_model(concepts, questions, 0.05)
    model_90, vectorizer_90 = create_language_model(concepts, questions, 0.1)
    save(model_100, vectorizer_100, 'tfidf_100_model', 'tfidf_100_vectors')
    save(model_95, vectorizer_95, 'tfidf_95_model', 'tfidf_95_vectors')
    save(model_90, vectorizer_90, 'tfidf_90_model', 'tfidf_90_vectors')
    log_info(f'training completed in {watch.time() - start}s\n')


@cli.command('normalize')
def normalize():
    def processor(doc):
        for line in normalize_doc_stream(doc):
            yield f'{line}'
    return processor


@cli.command('grammar')
@click.option(
    '-g', '--grammar', type=click.STRING, default='res/custom_ch_grammar.txt',
    help='use grammar file to correct words (default is "res/custom_ch_grammar.txt")'
)
def stopwords(grammar):
    def processor(doc):
        for line in correct_grammar_stream(doc, grammar):
            yield f'{line}'
    return processor


@cli.command('stopwords')
@click.option(
    '-l', '--language', type=click.STRING, default='res/custom_ch_stopwords.txt',
    help='stopwords file in pipeline (default is "res/custom_ch_stopwords.txt")'
)
def stopwords(language):
    def processor(doc):
        for line in remove_stopwords_stream(doc, language):
            yield f'{line}'
    return processor


@cli.command('stemm')
@click.option(
    '-l', '--language', type=click.STRING, default='de',
    help='choose vocabular language (default is "de")'
)
def stopwords(language):
    def processor(doc):
        for line in stemm_doc_stream(doc, language):
            yield f'{line}'
    return processor


@cli.command('lemm')
@click.option(
    '-l', '--language', type=click.STRING, default='de',
    help='choose vocabular language (default is "de")'
)
def stopwords(language):
    def processor(doc):
        for line in lemm_doc_stream(doc, language):
            yield f'{line}'
    return processor


if __name__ == '__main__':
    cli()
