#!/usr/bin/python3
'''
Script that starts a Flask web application:
'''

from flask import Flask, render_template

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

@app.route('/python/', defaults={'text': 'is cool'}, methods=['GET'], strict_slashes=False)
@app.route('/python/<text>', methods=['GET'], strict_slashes=False)
def python(text):
    # Replace underscores with spaces
    text = text.replace('_', ' ')
    return "Python {}".format(text)

@app.route('/number/<int:n>', methods=['GET'], strict_slashes=False)
def number(n):
    if isinstance(n, int):
        return "{} is a number".format(n)
    else:
        return "Invalid input. '{}' is not an integer.".format(n)

@app.route('/number_template/<int:n>', methods=['GET'], strict_slashes=False)
def number_template(n):
    if isinstance(n, int):
        return render_template('number.html', number=n)
    else:
        return "Invalid input. '{}' is not an integer.".format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


