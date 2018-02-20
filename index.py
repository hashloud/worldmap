# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, send_from_directory
#from flask_pbj import api, json, protobuf
from cosmos_pb2 import Person, Persons
from google.protobuf.json_format import MessageToJson
import copy

app = Flask('index')

persons = Persons()
board = list()
with open('pole.txt', 'r') as f:
    for line in f:
        row = list()
        board.append(row)
        for el in line.strip():
            row.append(el)

@app.route('/', methods=['GET'])
def index():
    board_with_persons = copy.deepcopy( board )
    for person in persons.person:
        board_with_persons[person.point.y][person.point.x] = board[person.point.y][person.point.x].upper()
    context = {
        'board': board_with_persons,
    }
    return render_template('board.html', **context)

@app.route('/json', methods=['GET'])
def json():
    response = app.response_class(
        response=MessageToJson(persons),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/cosmos', methods=['POST'])
#@api(json, protobuf(receives=Persons))
def cosmos():
    persons.ParseFromString(request.data)
    return 'Ok'
    #return str(persons)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

if __name__ == '__main__':
    app.run()
