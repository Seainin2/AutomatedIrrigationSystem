import flask
from flask import request, jsonify
from arduino import ArduinoNano
import pyfirmata
import time

app = flask.Flask(__name__)
app.config["DEBUG"] = True

incomes = [
    {'description':'salary','amount':5000},
    {'description':'side project','amount':400}
]

@app.route('/incomes', methods=['GET'])
def get_incomes():
    
    return jsonify(incomes)

@app.route('/incomes', methods=['POST'])
def add_income():
    incomes.append(request.get_json())
    return '', 204

app.run()

