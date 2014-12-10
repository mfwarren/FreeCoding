#!/usr/bin/env python
# imports go here
from __future__ import print_function
import threading
import thread
import time


doExit = 0

#
# Free Coding session for 2014-12-09
# Written by Matt Warren
#


class newThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("starting")
        print_time(self.name, self.counter, 5)
        print("done " + self.name)


def print_time(name, delay, counter):
    while counter:
        if doExit:
            thread.exit()
        time.sleep(delay)
        print("%s: %s" % (name, time.ctime(time.time())))
        counter -= 1

thread1 = newThread(1, 'thread1', 1)
thread2 = newThread(2, 'thread2', 2)

thread1.start()
thread2.start()

while thread2.isAlive():
    if not thread1.isAlive():
        doExit = 1
    pass

print("exit main thread")
