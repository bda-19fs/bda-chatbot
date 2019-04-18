#!/usr/bin/env python3
from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api


class Pipeline(Resource):
    def get(self):
        return {
            'Pipelines': [
                'TF-IDF',
                'TF-IDF with stemming'
            ]
        }


app = Flask(__name__)
cors = CORS(app, supports_credentials=True)
api = Api(app)

api.add_resource(Pipeline, '/')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
