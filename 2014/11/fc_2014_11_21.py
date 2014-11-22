#!/usr/bin/env python
# imports go here
from __future__ import print_function

#
# Free Coding session for 2014-11-21
# Written by Matt Warren
#

def hofstadter(i):
    if i < 1 or type(i) != int:
        raise ValueError("must be positive integer")
    if len(hofstadter.seq) > i:
        return hofstadter.seq[i]
    a = hofstadter(i - hofstadter(i-1)) + hofstadter(i - hofstadter(i-2))
    hofstadter.seq.append(a)
    return a
hofstadter.seq = [None, 1, 1]

print(hofstadter(10))
print(hofstadter(20))
print(hofstadter(100))

print([hofstadter(i) for i in xrange(1, 11)])

assert(hofstadter(1000), 502)
