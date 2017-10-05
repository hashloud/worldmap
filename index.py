# -*- coding: utf-8 -*-
from flask import Flask


app = Flask('index')


@app.route('/', methods=['GET'])
def index():
    return '<h1>It works</h1>'


if __name__ == '__main__':
    app.run()
