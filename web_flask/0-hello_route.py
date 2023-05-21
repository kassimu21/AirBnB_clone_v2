#!/usr/bin/python3
start Flask application
from flask import Flask
app = Flask('app')
app = Flask(__name__)



@app.route('/airbnb-onepage/')
def hello_world():
    #prints hello
    return "Hello HBNB!"


if __name__ ==
"__main__":
    app.run(host="0.0.0.0", port=5000)
