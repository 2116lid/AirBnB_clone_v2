#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models import *

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def li_state():
    """display a HTML page inside the Body tag"""
    statesli = list(storage.all(State).values())
    statesli.sort(key=lambda x: x.name)
    listate = {
        'states': statesli
    }
    return render_template('7-states_list.html', **listate)


@app.teardown_appcontext
def teardown(exc):
    """Call in this method storage.close()"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
