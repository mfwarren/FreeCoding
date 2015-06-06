#!/usr/bin/env python3
# imports go here
from collections import Counter
#
# Free Coding session for 2015-06-05
# Written by Matt Warren
#

def digit_counts(number):
    return Counter(str(number))

if __name__ == '__main__':
    print(digit_counts(1234534))
