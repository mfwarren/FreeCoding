#!/usr/bin/env python3
# imports go here
from dateutil.rrule import *
from dateutil.parser import *
import datetime

#
# Free Coding session for 2015-05-13
# Written by Matt Warren
#

if __name__ == '__main__':
    dates = list(rrule(DAILY, count=10, dtstart=datetime.date.today()))
    print(dates)

    print(parse("Thu Sep 25 10:36:28 MST 2015"))
