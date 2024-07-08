#!/usr/bin/python3
'''
script that starts a Flask web application:
'''

from flask import Flask

app = Flask(__name__, strict_slashes=False)

@app.route('/', methods=['GET'])
def home():
    return "Hello HBNB!"

@app.route('/hbnb', methods=['GET'])
def hbnb():
    return "HBNB"

@app.route('/c/<text>', methods=['GET'])
def c(text):
    # Replace underscores with spaces
    text = text.replace('_', ' ')
    return "C {}".format(text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

