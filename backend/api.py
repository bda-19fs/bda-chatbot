#!/usr/bin/env python3
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from lib.config import ui_config
from lib.preprocessing import nlp_strategy
from lib.algorithm import (
    load_tags_answers,
    algorithm_strategy
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
    dataset, _, _ = ui_config()
    data = request.get_json(force=True)
    nlp = nlp_strategy(data['config'])
    question = nlp(data['question'])
    algorithm = algorithm_strategy(data['config'])
    dataset = dataset[int(data['config']['dataset'])].lower()
    tags, answers, questions = load_tags_answers(dataset)
    tt, ta, tq, wt, wa, wq = algorithm(question, tags, answers, questions)
    return jsonify(
        nlp_question=question,
        tfidf_tags=tt, tfidf_answers=ta, tfidf_questions=tq,
        w2v_tags=wt, w2v_answers=wa, w2v_questions=wq
    )


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
