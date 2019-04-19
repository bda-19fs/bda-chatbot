#!/usr/bin/env python3
import logging
from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logging.getLogger('flask_cors').level = logging.DEBUG
CORS(app, resources=r'/api/*')

@app.route("/api/v1/pipelines/")
def list_pipelines():
    return jsonify(pipelines = [
        'TF-IDF',
        'TF-IDF with stemming'
    ])

@app.route("/api/v1/run", methods=['POST'])
def run():
    return jsonify(success = True)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
