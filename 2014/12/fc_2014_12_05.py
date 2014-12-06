#!/usr/bin/env python
# imports go here
from __future__ import print_function


#
# Free Coding session for 2014-12-05
# Written by Matt Warren
#


class Something:
    def __enter__(self):
        print("enter")
        return self

    def __exit__(self, type, value, traceback):
        print("exit")

    def p(self, s):
        print(s)


if __name__ == '__main__':
    with Something() as f:
        f.p("HI")
