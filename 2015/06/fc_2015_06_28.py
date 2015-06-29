#!/usr/bin/env python3
# imports go here
from flask import Flask

#
# Free Coding session for 2015-06-28
# Written by Matt Warren
#

class OtherStuff(object):
    about = "a tribute to"

    def __init__(self, title="crazy ones"):
        self.title = title

    def do_crazy_things(self):
        return "%s %s" % (OtherStuff.about, self.title)

class MyStuff(object):
    def __init__(self):
        self.other_stuff = OtherStuff()

    def crazy(self):
        return self.other_stuff.do_crazy_things()


app = Flask(__name__)

@app.route('/')
def index():
    ms = MyStuff()
    print(ms.crazy())
    return ms.crazy()

if __name__ == '__main__':
    app.run()
