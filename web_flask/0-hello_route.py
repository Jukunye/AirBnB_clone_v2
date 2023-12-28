#!/usr/bin/python3
"""
 script that starts a Flask web application:
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    """
    Route handler for the root path ("/").
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    """
    Starts the Flask app on 0.0.0.0 and port 5000.
    """
    app.run(host='0.0.0.0', port=5000)
