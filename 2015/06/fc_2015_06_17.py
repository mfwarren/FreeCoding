#!/usr/bin/env python3
# imports go here

#
# Free Coding session for 2015-06-17
# Written by Matt Warren
#

class Hi(object):
    def __init__(self, name):
        self.name = name

import threading

class Runner(threading.Thread):
    def __init__(self):
        super(Runner, self).__init__()
        self.hi = Hi("Matt")

    def run(self):
        print(self.hi.name)

if __name__ == '__main__':
    runner = Runner()
    runner.start()
