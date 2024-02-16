#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask, render_template

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


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def pyroute_func(text="is cool"):
    """displays 'python' followed by text"""
    text = text.replace("_", " ")
    return "Python %s" % text


@app.route('/number/<int:n>', strict_slashes=False)
def numroute_func(n):
    """displays 'n is number'"""
    if type(n) is int:
        return "%d is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def temroute_func(n):
    """displays H1 html tag"""
    if type(n) is int:
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def evodnum_func(n):
    """displays H1 tag witheven or odd"""
    if type(n) is int:
        return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
