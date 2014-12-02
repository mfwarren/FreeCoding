#!/usr/bin/env python
# imports go here
from __future__ import print_function
import datetime

#
# Free Coding session for 2014-12-01
# Written by Matt Warren
#


def days_until_christmas():
    today = datetime.date.today()
    christmas = datetime.date(year=today.year, month=12, day=25)
    if today > christmas:
        christmas = christmas + datetime.timedelta(days=365)
    return (christmas - today).days

print(days_until_christmas())
