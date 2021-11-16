import ansible
import docker
import requests
import os
import random
from flask import Flask, json, jsonify, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'random_string'

class ValidationError(ValueError):
    pass

@app.route('/shuffle', methods = ['GET'])
def shuffle(list_of_ints):
    shuffled_list = []
    shuffled_list = requests.get('url', params=query)
    random.shuffle(shuffled_list)
    return shuffled_list.json()

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'message': 'Page not found.'}), 404
@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({'message': 'Something broke.'}), 500


