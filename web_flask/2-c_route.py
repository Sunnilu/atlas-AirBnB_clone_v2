#!/usr/bin/python3
""" Flask web application with 3 view functions added """

from flask import Flask


app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    return "Hello HBNB!"


@app.route('/hbnb', methods=['GET'], strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', methods=['GET'], strict_slashes=False)
def c(text):
    # Replace underscores with spaces
    text = text.replace('_', ' ')
    return "C {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
