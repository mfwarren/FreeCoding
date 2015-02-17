#!/usr/bin/env python3
# imports go here
from statistics import mean, median, mode, stdev
from random import sample, uniform, paretovariate

#
# Free Coding session for 2015-02-16
# Written by Matt Warren
#

if __name__ == '__main__':
    print(mean([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(median([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(mode([1, 2, 3, 4, 5, 6, 7, 8, 9, 1]))
    print(stdev([1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(mean(sample([uniform(1, 10) for x in range(100000)], 10000)))
    print(mean(sample([paretovariate(10) for x in range(100000)], 10000)))
