#!/usr/bin/env python3
# imports go here

#
# Free Coding session for 2015-06-16
# Written by Matt Warren
#


class Delegate(object):
    def __init__(self, callback):
        self.callback = callback

    def finished(self):
        self.callback("DONE")


class Doer(object):
    def __init__(self):
        self.delegate = Delegate(self.done)

    def done(self, result):
        print(result)

    def start(self):
        print('working hard')
        if self.delegate:
            self.delegate.finished()


if __name__ == '__main__':
    doer = Doer()
    doer.start()
