#!/usr/bin/python3
"""
Starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """Display a HTML page listing all State objects"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)

    return render_template('9-states.html', states=sorted_states)


@app.route('/states/<state_id>', strict_slashes=False)
def state_cities(state_id):
    """Display a HTML page listing cities of a specific State"""
    state = storage.get(State, state_id)
    
    if state is None:
        return render_template('9-states.html', state_id="Not found!")

    cities = sorted(state.cities, key=lambda city: city.name)
    return render_template('9-states.html', state=state, cities=cities)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

