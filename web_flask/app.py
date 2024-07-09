#!/usr/bin/python3

from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def index():
    # Simulated data for demonstration
    states = [
        ("421a55f4-7d82-47d9-b54c-a76916479545", "Alabama"),
        ("421a55f4-7d82-47d9-b54c-a76916479546", "Arizona"),
        ("421a55f4-7d82-47d9-b54c-a76916479547", "California"),
        ("421a55f4-7d82-47d9-b54c-a76916479548", "Colorado"),
        ("421a55f4-7d82-47d9-b54c-a76916479549", "Florida"),
        ("421a55f4-7d82-47d9-b54c-a76916479550", "Georgia"),
        ("421a55f4-7d82-47d9-b54c-a76916479551", "Hawaii"),
        ("421a55f4-7d82-47d9-b54c-a76916479552", "Illinois"),
        ("421a55f4-7d82-47d9-b54c-a76916479553", "Indiana"),
        ("421a55f4-7d82-47d9-b54c-a76916479554", "Louisiana"),
        ("421a55f4-7d82-47d9-b54c-a76916479555", "Minnesota"),
        ("421a55f4-7d82-47d9-b54c-a76916479556", "Mississippi"),
        ("421a55f4-7d82-47d9-b54c-a76916479557", "Oregon"),
    ]
    return render_template('states.html', states=states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

