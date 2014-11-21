#!/usr/bin/env python
# imports go here
from __future__ import print_function

from math import sqrt

#
# Free Coding session for 2014-11-20
# Written by Matt Warren
#


def arithmetic_geometric_mean(a, b, tolerance=1e-10):
    an = (a + b) / 2
    bn = sqrt(a * b)

    while abs(an-bn) > tolerance:
        an, bn = (an + bn) / 2, sqrt(an * bn)
    return an

print(arithmetic_geometric_mean(0, 1))
print(arithmetic_geometric_mean(0, 100))
print(arithmetic_geometric_mean(2, 3))
print(arithmetic_geometric_mean(10, 20))
print(arithmetic_geometric_mean(24, 6))
