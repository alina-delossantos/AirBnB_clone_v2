#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return('HBNB')


@app.route('/c/<string:text>', strict_slashes=False)
def c_is(text):
    return('C {}'.format(text.replace('_', ' ')))


if __name__ == '__main__':
    app.run()
