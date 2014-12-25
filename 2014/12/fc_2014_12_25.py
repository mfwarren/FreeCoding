#!/usr/bin/env python3
# imports go here
from flask import Flask
from flask.ext.script import Manager

#
# Free Coding session for 2014-12-25
# Written by Matt Warren
#


app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def index():
    return "<h1>Merry Christmas</h1>"

if __name__ == '__main__':
    manager.run()
