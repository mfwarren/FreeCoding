#!/usr/bin/env python3
# imports go here

#
# Free Coding session for 2015-03-19
# Written by Matt Warren
#

def foo():
    a, b = 1, 2
    a, b = b, a
    return a, b


if __name__ == '__main__':
    a, b = foo()

    print(a)
    print(b)

    #not sure what to code today

    def inner_func(a, b):
        a, b = b, a
        return a, b

    a, b = inner_func(a, b)

    print(a)
    print(b)

    
