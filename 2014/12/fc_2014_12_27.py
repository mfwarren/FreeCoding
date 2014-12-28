#!/usr/bin/env python3
# imports go here
from flask import Flask

#
# Free Coding session for 2014-12-27
# Written by Matt Warren
#


app = Flask(__name__)


@app.route('/')
def index():
    return "HELLO"

if __name__ == '__main__':
    app.run()
