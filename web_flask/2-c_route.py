#!/usr/bin/python3
"""script that starts a Flask web application"""
from cgitb import text
from flask import Flask


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """display “Hello HBNB!”"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hello_2():
    """display “HBNB”"""
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def hello_3():
    """display “C ” followed by the text variable"""
    text = text.replace("_", " ")
    return "C {}".format(text)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
