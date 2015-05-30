#!/usr/bin/env python3
# imports go here
import statistics
import random

#
# Free Coding session for 2015-05-29
# Written by Matt Warren
#

numbers = [random.randrange(1000) for i in range(1000)]

print(statistics.pstdev(numbers))
