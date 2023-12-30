#!/usr/bin/python3
"""
 script that starts a Flask web application:
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def remove_session(error):
    """This will close the session when the application is out of context"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def fetch_states():
    """Fetches all states in the database"""
    states_list = storage.all()
    return render_template("7-states_list.html", states_list=states_list)


if __name__ == '__main__':
    """
    Starts the Flask app on 0.0.0.0 and port 5000.
    """
    app.run(host='0.0.0.0', port=5000, debug=True)
