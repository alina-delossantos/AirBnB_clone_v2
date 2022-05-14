#!/usr/bin/python3
"""script that starts a Flask web application"""
from cgitb import text
from flask import Flask, render_template


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
def c(text):
    """display “C ” followed by the text variable"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/(<text>)', strict_slashes=False)
def python(text="is cool"):
    """display “Python ”, followed by the value of the text variable"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    """display ”n is a number” only if n is an integer"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def template(n):
    """display a HTML page only if n is an integer"""
    return render_template("5-number.html", num=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
