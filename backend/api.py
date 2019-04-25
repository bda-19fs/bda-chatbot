#!/usr/bin/env python3
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from bda_core.use_cases.prediction.algorithm import (
    load_tags_answers,
    algorithm_strategy
)
from lib.config import (
    ui_config
)


app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logging.getLogger('flask_cors').level = logging.DEBUG
CORS(app, resources=r'/api/*')

@app.route('/api/v1/pipelines/')
def list_pipelines():
    dataset, algorithm, domain_limit = ui_config()
    return jsonify(dataset=dataset, algorithm=algorithm, domain_limit=domain_limit)

@app.route('/api/v1/run', methods=['POST'])
def run():
    data = request.get_json(force=True)
    algorithm = algorithm_strategy(data['config'])
    tags, answers = load_tags_answers()
    tfidf_tags, tfidf_answers = algorithm(data['question'], tags, answers)
    return jsonify(tfidf_tags=tfidf_tags, tfidf_answers=tfidf_answers, skip_gram=[])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
