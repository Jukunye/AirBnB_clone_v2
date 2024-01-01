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


@app.route("/states", strict_slashes=False)
def fetch_states():
    """Fetches all states in the database"""
    states_list = storage.all('State')
    return render_template("9-states.html", states_list=states_list)


@app.route("/states/<id>", strict_slashes=False)
def fetch_cities(id):
    """Fetches all states and cities in the database"""
    states_list = storage.all('State')
    cities_list = storage.all('City')

    val = "State.{}".format(id)

    cities = []

    if val in states_list:
        for key, city in cities_list.items():
            if city.state_id == id:
                cities.append(city)
    else:
        cities = None
    
    return render_template("9-states.html", cities=cities)


if __name__ == '__main__':
    """
    Starts the Flask app on 0.0.0.0 and port 5000.
    """
    app.run(host='0.0.0.0', port=5000, debug=True)
