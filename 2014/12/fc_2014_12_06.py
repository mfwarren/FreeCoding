#!/usr/bin/env python
# imports go here
from __future__ import print_function


#
# Free Coding session for 2014-12-06
# Written by Matt Warren
#


a = lambda b: print(b)


a("HI")

range = (lambda x, val: x(x, val))(lambda y, val: y(y, val - 1) if val > 0 and (print(val) or True) else print("Liftoff!"), 10)

range(10)
# print()
