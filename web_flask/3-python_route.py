#!/usr/bin/python3
"""
 script that starts a Flask web application:
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Route handler for the root path ("/").
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route handler for the root path ("/hbnb").
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_fun(text):
    """
    Route handler for the root path ("/c").
    """
    return "C {}".format(text).replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_func(text="is cool"):
    """
    Route handler for the root path ("/python").
    """
    return "python {}".format(text).replace('_', ' ')


if __name__ == '__main__':
    """
    Starts the Flask app on 0.0.0.0 and port 5000.
    """
    app.run(host='0.0.0.0', port=5000)
