#!/usr/bin/env python3
# imports go here
import fcntl

#
# Free Coding session for 2015-06-20
# Written by Matt Warren
#

with open('/tmp/lock', 'w') as fd:
    fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    print("something")

    fcntl.flock(fd, fcntl.LOCK_EX)  # deadlock?
    print("Not printing?")


fd = open('/tmp/lock', 'w')

fcntl.flock(fd, fcntl.LOCK_EX)
print("something")

fcntl.flock(fd, fcntl.LOCK_EX)  # deadlock?
print("Not printing?")
