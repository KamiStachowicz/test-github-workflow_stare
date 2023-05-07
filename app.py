"""
This module contains a Flask application that displays a greeting message.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World! Greetings from Flask!</h1>'

if __name__ == "__main__":
    app.run(debug=True)
