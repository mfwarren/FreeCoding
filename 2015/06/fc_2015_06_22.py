#!/usr/bin/env python3
# imports go here

#
# Free Coding session for 2015-06-22
# Written by Matt Warren
#

from theano import *
import theano.tensor as T

x = T.dscalar('x')
y = T.dscalar('y')
z = x + y
f = function([x, y], z)

print(f(234, 2342))


#a ** 2 + b ** 2 + 2 * a * b.

a = T.vector()
b = T.vector()
out = a ** 2 + b ** 2 + 2 * a * b
f2 = function([a, b], out)

print(f2([1, 2, 3], [5, 6, 7]))
