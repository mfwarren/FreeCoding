#!/usr/bin/env python3
# imports go here

#
# Free Coding session for 2015-06-25
# Written by Matt Warren
#

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world!'

app.run()
