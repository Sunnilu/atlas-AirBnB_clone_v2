#!/usr/bin/python3
""" 7. Start flask service that does something. """

from flask import Flask, render_template

app = Flask(__name__)

# Route to display "Hello HBNB!"
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

# Route to display "HBNB"
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

# Route to display "C <text>"
@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return 'C ' + text.replace('_', ' ')

# Route to display "Python <text>"
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    return 'Python ' + text.replace('_', ' ')

# Route to display "n is a number" if n is an integer
@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return '{} is a number'.format(n)

# Route to display a HTML page if n is an integer
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('number.html', n=n)

# Route to display a HTML page indicating if n is even or odd
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    odd_or_even = 'even' if n % 2 == 0 else 'odd'
    return render_template('number_odd_even.html', n=n, odd_or_even=odd_or_even)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
