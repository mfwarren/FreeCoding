#!/usr/bin/env python
# imports go here
from __future__ import print_function
#
# Free Coding session for 2014-11-16
# Written by Matt Warren
#


def foo():
    print("HI")

    [print(i) for i in xrange(1, 10, 3)]
    [print(i) for i in xrange(10, 1, -1)]

    a = 'asdfasdfasdfiwoneva'
    [print(a[i]) for i in xrange(0, len(a), 4)]
    print(''.join([a[i] for i in xrange(0, len(a), 4)]))

    [print(i) for i, j in enumerate(xrange(0, len(a))) if a[i] == 'a']
    [print(i) for i, j in enumerate(a) if j == 'a']

    print('boo')


foo()
