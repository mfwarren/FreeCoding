#!/usr/bin/env python3
# imports go here
from collections import namedtuple

#
# Free Coding session for 2015-03-25
# Written by Matt Warren
#

Point = namedtuple('Point', ['x', 'y'])
Item = namedtuple('Item', ['price', 'quantity'], verbose=True)
Measure = namedtuple('Measure', 'temperature, rh, def', rename=True)
try:
    Measure2 = namedtuple('Measure', 'temperature, rh, def', rename=False)
except ValueError:
    print('cannot create named tuple that has reserved words or non-valid variable names')

if __name__ == '__main__':
    p = Point(1, 2)
    print(p)
    p = p._replace(x=4)

    print(p._asdict())

    print('p + p = ', (p + p))
    print('p * 3 = ', p * 3)

    m = Measure(2.55, 10.23, 44)
    print(m)
    print(dir(m))
