#!/usr/bin/env python3
# imports go here
import time
import sys

#
# Free Coding session for 2015-04-16
# Written by Matt Warren
#

def print_progress(percent):
    count = int(percent * 20 / 100)
    space = 20 - count
    sys.stdout.write("\r["+("="*count) + ">" + (' ' * space) + ']')
    sys.stdout.flush()

if __name__ == '__main__':
    for i in range(100):
        print_progress(i)
        time.sleep(0.02)
    print("")
