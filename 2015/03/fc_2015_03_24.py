#!/usr/bin/env python3
# imports go here
import queue

#
# Free Coding session for 2015-03-24
# Written by Matt Warren
#

class Worker(object):
    def __init__(self, *args, **kwargs):
        self.queue = queue.Queue()
        self.args = args
        self.kwargs = kwargs

    def add_task(self, task):
        self.queue.put(task)

    def __call__(self):
        while not self.queue.empty():
            next_task = self.queue.get()
            success = next_task(*self.args, **self.kwargs)
            if not success:
                self.add_task(next_task)  # try again
            else:
                print(success)

def add(x, y):
    return x + y

def mult(x, y):
    return x * y

if __name__ == '__main__':
    w = Worker(2, 4)
    w.add_task(add)
    w.add_task(mult)

    w()
