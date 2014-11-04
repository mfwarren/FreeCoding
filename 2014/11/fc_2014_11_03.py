#!/usr/bin/env python
# imports go here
import os

#
# Free Coding session for 2014-11-03
# Written by Matt Warren
#

if __name__ == '__main__':
    for filename in os.listdir('.'):
        if filename.startswith('fc'):
            _, year, month, _ = filename.split('_')
            if not os.path.exists(year):
                os.mkdir(year)
            if not os.path.exists(os.path.join(year, month)):
                os.mkdir(os.path.join(year, month))

            os.rename(filename, os.path.join(year, month, filename))
