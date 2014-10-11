#!/usr/bin/env python
#imports go here

#
# Free Coding session for 2014-10-10
# Written by Matt Warren
#


def co_routine(fun):
    try:
        while True:
            n = fun((yield))
            # n = fun(n).next()
            print "received", n
    except GeneratorExit:
        print "finished"

def double(n):
    return n * 2

if __name__=='__main__':
    c = co_routine(double)
    c.next()
    for i in xrange(5, 10, 1):
        print c.send(i)
    c.close()
