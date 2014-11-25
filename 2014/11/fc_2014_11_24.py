#!/usr/bin/env python
# imports go here
from __future__ import print_function
import random


#
# Free Coding session for 2014-11-24
# Written by Matt Warren
#


class Pump:
    def __init__(self, reliability=1, rate=200, stdev=2):
        self.reliability = reliability
        self.rate = rate
        self.stdev = stdev

    def instantanious_rate(self):
        if random.random() > self.reliability:
            return 0
        return random.gauss(self.rate, self.stdev)


best_rate = 0
pumps = [Pump(.5, 100, 1), Pump(.6, 222, 11)]

running_sum = 0
available_count = 0

num_loops = 10000
for i in xrange(num_loops):
    # running pumps in parallel
    val = sum([p.instantanious_rate() for p in pumps])
    if val > best_rate:
        best_rate = val
    running_sum += val
    if val > 0:
        available_count += 1

print("Best rate:", best_rate)
print("Avg. rate:", running_sum/num_loops)
print("Availability:", float(available_count)/num_loops)
