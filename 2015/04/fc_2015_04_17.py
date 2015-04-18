#!/usr/bin/env python3
# coding: utf8
# imports go here
import sys
import time
#
# Free Coding session for 2015-04-17
# Written by Matt Warren
#


def spinner():
    while True:
        for c in '–\|/—\|/':
            sys.stdout.write("\r%s" % c)
            sys.stdout.flush()
            time.sleep(0.1)

if __name__ == '__main__':
    spinner()
