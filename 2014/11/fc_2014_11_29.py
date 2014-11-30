#!/usr/bin/env python
# imports go here
from __future__ import print_function


#
# Free Coding session for 2014-11-29
# Written by Matt Warren
#


def foo(x):
    if x == 1:
        return 2
    else:
        return foo(x-1)*2

print(foo(10))
