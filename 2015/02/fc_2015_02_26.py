#!/usr/bin/env python3
# imports go here
from gevent import monkey
monkey.patch_all()

import time
from threading import Thread
from github import Github
import os


from flask import Flask, render_template
from flask.ext.socketio import SocketIO

#
# Free Coding session for 2015-02-26
# Written by Matt Warren
#

app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdivbaiwubdfilsudbxv'
app.debug = True
socketio = SocketIO(app)
thread = None
# hub = Github()
hub = Github(os.environ['GITHUB_USERNAME'], os.environ['GITHUB_PASSWORD'])

USERS = [
    'mfwarren'
]


def get_public_events():
    events = {}
    for u in USERS:
        hub_user = hub.get_user('mfwarren')
        events[u] = hub_user.get_public_events()[0].raw_data
    return events


def background_thread():
    while True:
        events = get_public_events()
        print(events)
        socketio.emit('response', {'data': 'events', 'events': events}, namespace='')
        time.sleep(10)


@app.route('/')
def index():
    global thread
    if thread is None:
        thread = Thread(target=background_thread)
        thread.start()
    return render_template('github_index.html')


@socketio.on('event')
def message(message):
    pass  # need side effects from having this here

if __name__ == '__main__':
    socketio.run(app)
