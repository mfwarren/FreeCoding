#!/usr/bin/env python3
# imports go here
from flask import Flask, render_template
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap

#
# Free Coding session for 2014-12-25
# Written by Matt Warren
#


app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    manager.run()
