#!/usr/bin/env python
#imports go here
import ipdb

#
# Free Coding session for 2014-10-08
# Written by Matt Warren
#

def foo(msg):
    """prints something then raises an exception"""
    # ipdb.set_trace()
    print msg
    try:
        raise Exception("WAT?!")
    except Exception, e:
        ipdb.set_trace()

if __name__=='__main__':
    ipdb.pm()
    foo("Hello World")
