#!/usr/bin/env python3
# imports go here
import sys
import time

#
# Free Coding session for 2015-01-29
# Written by Matt Warren
#


if __name__ == '__main__':
    for i in range(100, 0, -1):
        numstr = "%d" % i
        sys.stdout.write(numstr)
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b'*len(numstr))
        print("Surprise!")
