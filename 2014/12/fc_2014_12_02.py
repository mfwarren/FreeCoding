#!/usr/bin/env python
# imports go here
from __future__ import print_function


#
# Free Coding session for 2014-12-02
# Written by Matt Warren
#

# making something convoluted


def foo(f, a):
    f(a())


def bar(s):
    return s


def ok():
    def jam():
        return "OK"
    return jam


class Asdf:
    def __init__(self, k, j):
        self.k = bar(k)
        self.p = j()

    def jim(self):
        return foo(self.k, self.p)

if __name__ == '__main__':
    a = Asdf(print, ok)
    a.jim()
