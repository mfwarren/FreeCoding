#!/usr/bin/env python
# imports go here
from __future__ import print_function
import math

#
# Free Coding session for 2014-11-25
# Written by Matt Warren
#

def mandelbrot(z, c, n=40):
    if abs(z) > 1000:
        return float('nan')
    else:
        if n > 0:
            return mandelbrot(z**4+c, c, n-1)
        else:
            return z**4+c

print("\n".join(["".join(["#" if not math.isnan(mandelbrot(0, x+1j*y).real) else " "
                         for x in [a * 0.02 for a in xrange(-80, 30)]])
                for y in [a * 0.05 for a in xrange(-20, 20)]]))
