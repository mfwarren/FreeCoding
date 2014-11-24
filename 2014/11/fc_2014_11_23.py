#!/usr/bin/env python
# imports go here
from __future__ import print_function

import math
import random

#
# Free Coding session for 2014-11-23
# Written by Matt Warren
#


def random_pair():
    # random numbers between 0:1
    return (random.random(), random.random())


def calc_pi(iterations=100000):
    return 4.0 * sum(math.hypot(*random_pair()) < 1 for p in xrange(iterations)) / float(iterations)


if __name__ == '__main__':
    print(calc_pi())
