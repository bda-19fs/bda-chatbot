from flask import Flask, request
from rasa_nlu.model import Interpreter
import json
import sys

app = Flask(__name__)
interpreter = Interpreter.load('./models/current/nlu')

@app.route('/')
def hello():
  return 'I am alive'


@app.route('/query')
def query():
  message = request.args.get('msg')
  result = interpreter.parse(message)
  
  return json.dumps(result, indent=2)
