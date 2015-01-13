#!/usr/bin/env python3
# imports go here
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

#
# Free Coding session for 2015-01-12
# Written by Matt Warren
#

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
