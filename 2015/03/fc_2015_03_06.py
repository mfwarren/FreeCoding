#!/usr/bin/env python3
# imports go here
import inspect
import importlib

#
# Free Coding session for 2015-03-06
# Written by Matt Warren
#


class Foo(object):
    def __init__(self):
        self.name == 'me'

if __name__ == '__main__':
    f = importlib.__import__('fc_2015_03_06')
    print(inspect.getsource(f))
