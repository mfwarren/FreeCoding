#!/usr/bin/env python
# imports go here
from __future__ import print_function
import random

#
# Free Coding session for 2014-12-08
# Written by Matt Warren
#


def foo(s):
    return random.randint(0, s)

foo2 = lambda s: random.randint(0, s)

ds = {
    'a': lambda a: random.randint(0, a),
    'b': lambda a: random.randint(0, a*2),
    'c': lambda a: random.randint(0, a*3)
}

da = [lambda a: random.randint(0, a),
      lambda a: random.randint(0, a*2),
      lambda a: random.randint(0, a*3)
      ]

if __name__ == '__main__':
    print(foo(10))
    print(foo2(10))
    print(ds['a'](100))
    print(ds['b'](100))
    print(da[1](200))
