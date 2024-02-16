#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def route_func():
    """displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnbroute_func():
    """displays 'HBNB'"""
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def croute_func(text):
    """displays 'C' followed by text"""
    text = text.replace("_", " ")
    return "C %s" % text


if __name__ == "__main__":
    app.run(host="0.0.0.0")