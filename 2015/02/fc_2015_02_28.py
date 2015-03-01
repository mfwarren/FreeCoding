#!/usr/bin/env python3
# imports go here
import datetime

#
# Free Coding session for 2015-02-28
# Written by Matt Warren
#

year = datetime.date.today().year


if __name__ == '__main__':
    if year % 4 == 0:
        print("this is leap year")
    else:
        print("%d not a leap year" % year)
