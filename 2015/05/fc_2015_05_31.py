#!/usr/bin/env python3
# imports go here

#
# Free Coding session for 2015-05-31
# Written by Matt Warren
#

def factors(x):
    values = []
    cursor = x
    i = 2
    while i <= cursor:
        v = cursor / i
        if int(v) == v:
            cursor = v
            values.append(i)
        else:
            i += 1
    return values

if __name__ == '__main__':
    print(factors(302))
    print(factors(304))
    print(factors(30473456))
