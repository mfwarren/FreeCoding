#!/usr/bin/env python3
# imports go here
import os
from flask import Flask
from flask.ext.script import Shell, Manager

#
# Free Coding session for 2015-01-25
# Written by Matt Warren
#


if os.path.isfile('.env'):
    for line in open('.env'):
        line = line.split('=')
        if len(line == 2):
            os.environ[line[0]] = line[1]


app = Flask(__name__)
manager = Manager(app)


def make_shell_context():
    return dict(app=app)
manager.add_command('shell', Shell(make_context=make_shell_context))


@app.route('/')
def index():
    return "HI"

if __name__ == '__main__':
    manager.run()
