#!/usr/bin/python3

from flask import Flask

app = Flask(__name__, strict_slashes=False)

@app.route('/', methods=['GET'])
def hello_hbnb():
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
