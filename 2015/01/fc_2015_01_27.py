#!/usr/bin/env python3
# imports go here
import sys
import time


#
# Free Coding session for 2015-01-27
# Written by Matt Warren
#

def spinning_cursor():
    while True:
        for cursor in '|/–\\':
            yield cursor

spinner = spinning_cursor()

if __name__ == '__main__':
    for c in spinner:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')
