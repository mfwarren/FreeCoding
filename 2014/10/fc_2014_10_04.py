#!/usr/bin/env python
#imports go here

#
# Free Coding session for 2014-10-04
# Written by Matt Warren
#


def sum(x, y):
    return x+y

def product(x, y):
    return x * y

def factorial(n):
    return reduce(product, xrange(1, n+1))

print reduce(sum, xrange(10))

print product(8, 7)
print reduce(product, xrange(1,10))
print factorial(10)

def fib():
    # generator for fibonacci sequence
    n_2, n_1 = 0, 1
    while True:
        yield n_2
        n_1 = n_1 + n_2
        yield n_1
        n_2 = n_1 + n_2

for i, n in enumerate(fib()):
    print i, n
    if n > 10000:
        break

from itertools import islice

def nth_fib(n):
    return islice(fib(), n, n+1).next()

print '19th Fibonacci number:', nth_fib(19)
