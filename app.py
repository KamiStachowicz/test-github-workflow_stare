"""
This module contains a Flask application that displays a greeting message.
"""
import sys

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World! Greetings from Flask!</h1>'

def print_python_version():
    """
    Function printing the Python version.
    """
    print(sys.version)

if __name__ == "__main__":
    app.run(debug=True)
