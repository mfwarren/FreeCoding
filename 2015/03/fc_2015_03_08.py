#!/usr/bin/env python3
# imports go here
from fn import op, _

#
# Free Coding session for 2015-03-08
# Written by Matt Warren
#


def add(first):
    def add(second):
        return first + second
    return add

if __name__ == '__main__':
    print((_ + 3)(5))
    print((_ + _)(3, 5))
    print(op.curry(add, 12, 1))
