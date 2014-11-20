#!/usr/bin/env python
# imports go here
import random

#
# Free Coding session for 2014-11-19
# Written by Matt Warren
#

target = random.randint(0, 10)
guess = 0

while target != guess:
    guess = int(input('Guess a number 1-10:'))
print "Got it!"
