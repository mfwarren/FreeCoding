#!/usr/bin/env python3
# imports go here

#
# Free Coding session for 2015-06-01
# Written by Matt Warren
#

def series(accuracy=0.0001):
    prev = 0
    current = 0
    i = 1
    while True:
        prev = current
        if i % 2 == 1:
            current += 1.0/i
        else:
            current -= 1.0/i
        i += 1
        print(current)
        if abs(current - prev) < accuracy:
            break


if __name__ == '__main__':
    # print(math.exp(10))
    print(series())
