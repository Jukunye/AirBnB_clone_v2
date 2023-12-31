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


@app.route("/cities_by_states", strict_slashes=False)
def fetch_states():
    """Fetches all states and cities in the database"""
    states_list = storage.all('State')
    cities_list = storage.all('City')

    return render_template(
        "8-cities_by_states.html",
        states_list=states_list,
        cities_list=cities_list)


if __name__ == '__main__':
    """
    Starts the Flask app on 0.0.0.0 and port 5000.
    """
    app.run(host='0.0.0.0', port=5000)
