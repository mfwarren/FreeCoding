#!/usr/bin/env python3
# imports go here
import contextlib

#
# Free Coding session for 2015-04-19
# Written by Matt Warren
#

@contextlib.contextmanager
def foo():
    print("HI")
    try:
        yield 'Matt'
    except:
        pass

if __name__ == '__main__':
    with foo() as name:
        print(name)
        raise Exception("burried")
