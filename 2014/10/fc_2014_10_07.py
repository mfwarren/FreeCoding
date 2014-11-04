#!/usr/bin/env python
#imports go here

#
# Free Coding session for 2014-10-07
# Written by Matt Warren
#

def foo():
    pass


def outer():
    s = 1
    def inner():
        return s
    return inner


def print_args(f):
    def inner(*args, **kwargs):
        print args
        print kwargs
        return f(*args, **kwargs)
    return inner

@print_args
def bar(s):
    return s.upper()

if __name__=='__main__':
    print issubclass(foo.__class__, object)

    print outer()
    print outer()()

    print bar('hi')
