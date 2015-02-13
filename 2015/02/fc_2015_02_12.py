#!/usr/bin/env python3
# imports go here
from gevent import monkey
monkey.patch_all()

import time
from threading import Thread
import urllib

from flask import Flask, render_template
from flask.ext.socketio import SocketIO

#
# Free Coding session for 2015-02-12
# Written by Matt Warren
#

app = Flask(__name__)
app.config['SECRET_KEY'] = 'oaisndviouhwdnvilxuanbodni'
socketio = SocketIO(app)
thread = None

SITES = [
    'http://halotis.com',
    'http://mattwarren.co'
]


def update_website_status():
    site_status = {}
    for site in SITES:
        site_status[site] = urllib.urlopen(site).getcode()
    return site_status


def background_thread():
    """Example of how to send server generated events to clients."""
    while True:
        status = update_website_status()
        print(status)
        socketio.emit('my response',
                      {'data': 'Server generated event', 'statuses': status},
                      namespace='')
        time.sleep(10)


@app.route('/')
def index():
    global thread
    if thread is None:
        thread = Thread(target=background_thread)
        thread.start()
    return render_template('index.html')


@socketio.on('event')
def message(message):
    pass  # this seems to initialze the socket io


if __name__ == '__main__':
    socketio.run(app)
