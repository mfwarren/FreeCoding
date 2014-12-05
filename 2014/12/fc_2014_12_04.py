#!/usr/bin/env python
# imports go here
from __future__ import print_function

#
# Free Coding session for 2014-12-04
# Written by Matt Warren
#


def foo(s):
    ba = bytearray(s)
    for i in xrange(len(s)/2):
        ba[i], ba[-(1+i)] = ba[-(1+i)], ba[i]
    return str(ba)


if __name__ == '__main__':
    print(foo("HELLO"))
    print(foo("ASDF"))
