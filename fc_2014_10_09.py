#!/usr/bin/env python
#imports go here
import time

#
# Free Coding session for 2014-10-09
# Written by Matt Warren
#

def foo(func):
    state = "MY STATE"
    def foo():
        print "About to start this awesome function"
        t = time.time()
        result = func()
        elapsed = time.time() - t
        print "Elapsed time: ", elapsed
        print "FUnction is complete"
        return result
    return foo


@foo
def counting():
    n = 0
    for i in xrange(1000000):
        n = n + 1

if __name__=='__main__':
    counting()
