#!/usr/bin/env python3
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from joblib import load
from bda_core.use_cases.prediction.utils import predict_n_answers


app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logging.getLogger('flask_cors').level = logging.DEBUG
CORS(app, resources=r'/api/*')

@app.route('/api/v1/pipelines/')
def list_pipelines():
    return jsonify(pipelines = [
        'TF-IDF',
        'TF-IDF with stemming'
    ])

@app.route('/api/v1/run', methods=['POST'])
def run():
    data = request.get_json(force=True)
    language_model = load('models/language_model.joblib')
    vectorizer = load('models/language_modelvec.joblib')
    answers = file_as_list('models/stackexchange_answers.txt')
    questions = [data['question']]
    result = predict_n_answers(language_model, vectorizer, questions, answers, 10)
    return jsonify(result=result)

def file_as_list(file):
    with open(file, 'r', encoding='utf-8') as file:
        return list(map(lambda line: line.strip(), file.readlines()))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
