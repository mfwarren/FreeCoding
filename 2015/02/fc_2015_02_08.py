#!/usr/bin/env python3
# imports go here
from contextlib import contextmanager


#
# Free Coding session for 2015-02-08
# Written by Matt Warren
#


@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

if __name__ == '__main__':
    with tag('html'):
        with tag('body'):
            with tag('h1'):
                print("Title")
