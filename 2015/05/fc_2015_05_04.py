#!/usr/bin/env python3
# imports go here
import sched
import time

#
# Free Coding session for 2015-05-04
# Written by Matt Warren
#

scheduler = sched.scheduler(time.time, time.sleep)

def print_time():
    print(time.time())
    return True

scheduler.enter(3, 1, print_time)
scheduler.enter(5, 1, print_time)

print(scheduler.queue)
scheduler.run()  # blocking until all scheduled things finish
print("done")
