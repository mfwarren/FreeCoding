#!/usr/bin/env python
# imports go here
import datetime

#
# Free Coding session for 2014-11-18
# Written by Matt Warren
#


def foo():
    d = datetime.datetime.now()

    print d

    print d + datetime.timedelta(hours=1)

    print d.strftime("%Y-%m-%d")
    print [(d+datetime.timedelta(hours=i)).strftime("%H:%M:%S") for i in xrange(1, 10)]

foo()
