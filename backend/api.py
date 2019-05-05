#!/usr/bin/env python3
import pickle
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_caching import Cache


from gensim.models import Word2Vec
from bda_core.use_cases.prediction.utils import (
    predict_n_answers,
    predict_n_w2v_answers
)
from lib.config import ui_config
from lib.preprocessing import nlp_strategy
from lib.loader import (
    load_tags_answers,
    get_model_components,
    load_models
)


logging.basicConfig(level=logging.INFO)
logging.getLogger('flask_cors').level = logging.DEBUG


app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
cors = CORS(app, resources=r'/api/*')


@app.route('/api/v1/pipelines/')
def list_pipelines():
    dataset, algorithm, domain_limit = ui_config()
    return jsonify(dataset=dataset, algorithm=algorithm, domain_limit=domain_limit)


@app.route('/api/v1/run', methods=['POST'])
def run():
    dataset, _, _ = ui_config()
    data = request.get_json(force=True)
    nlp = nlp_strategy(data['config'])
    question = nlp(data['question'])
    dataset = dataset[int(data['config']['dataset'])].lower()
    tags, answers, questions = load_tags_answers(dataset)
    language_model_tfidf, vectors_tfidf, language_model_w2v, vectors_w2v = load_models_with_caching(data['config'])
    tt, ta, tq = predict_n_answers(language_model_tfidf, vectors_tfidf, [question], tags, answers, questions, 10)
    wt, wa, wq = predict_n_w2v_answers(question, language_model_w2v, vectors_w2v, tags, answers, questions, 10)
    return jsonify(
        nlp_question=question,
        tfidf_tags=tt, tfidf_answers=ta, tfidf_questions=tq,
        w2v_tags=wt, w2v_answers=wa, w2v_questions=wq
    )


@cache.memoize(timeout=0)
def load_models_with_caching(config):
    folder, model, vectors = get_model_components(config)
    return load_models(folder, model, vectors)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
