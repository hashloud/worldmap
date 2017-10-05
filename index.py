# -*- coding: utf-8 -*-
from flask import Flask, render_template


app = Flask('index')


@app.route('/', methods=['GET'])
def index():
    board = list()
    with open('pole.txt', 'r') as f:
        i = 0
        for line in f:
            board.append(list())
            for el in line.strip():
                board[i].append(el)
            i += 1

    context = {
        'board': board,
    }
    return render_template('board.html', **context)


if __name__ == '__main__':
    app.run()
