#!/usr/bin/env python3
# imports go here
import math

#
# Free Coding session for 2015-05-30
# Written by Matt Warren
#


#calculate e^x using a converging series

def e_power(x, accuracy=0.1):
    prev = 0
    current = 1
    counter = 1
    while current - prev > accuracy:
        prev = current
        current += ((x**counter) / math.factorial(counter))
        counter += 1
        print(current)

if __name__ == '__main__':
    # print(math.exp(10))
    print(e_power(10))
