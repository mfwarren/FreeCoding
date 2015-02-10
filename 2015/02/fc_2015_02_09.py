#!/usr/bin/env python3
# imports go here
import random
from contextlib import ExitStack

#
# Free Coding session for 2015-02-09
# Written by Matt Warren
#


def do_something_interesting():
    print("Hard work")
    return random.randint(0, 1)


def cleanup_stuff(msg):
    print(msg)

if __name__ == '__main__':
    with ExitStack() as es:
        es.callback(cleanup_stuff, 'ids to clean')
        result = do_something_interesting()
        if result == 0:
            es.pop_all()  # cancel the cleanup
