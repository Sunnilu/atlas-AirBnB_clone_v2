#!/usr/bin/python3

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def index():
    states = []
    all_states = storage.all(State).values()
    for state in all_states:
        states.append((state.id, state.name))
    return render_template('states.html', states=states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


