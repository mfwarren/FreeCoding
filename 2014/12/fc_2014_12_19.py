#!/usr/bin/env python3
# imports go here
import os

#
# Free Coding session for 2014-12-19
# Written by Matt Warren
#


if __name__ == '__main__':
    for filename in os.listdir('.'):
        if os.path.isfile(filename):
            with open(filename) as f:
                try:
                    text = f.read()
                    print(filename + ": " + str(len(text.split())))
                except:
                    print(filename + ": not a text file")
