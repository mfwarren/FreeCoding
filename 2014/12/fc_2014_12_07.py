#!/usr/bin/env python
# imports go here
from __future__ import print_function
#
# Free Coding session for 2014-12-07
# Written by Matt Warren
#


myFunc = (lambda(new):
    new.function(
        (lambda a, b: a + b).func_code, {}, 'myFunc'
    )
)(__import__('new'))

print(myFunc(1, 2))
print(__import__('new'))
n = __import__('new')

print(dir(n))

# print(n.function())


myFunc2 = lambda a, b: a + b

print(myFunc2(1, 2))


def func(a):
    def func2(self, b):
        self.a = self.a * b
        return self.a
    return func2

f2 = func(3)
print(dir(f2))
print(f2.func2(2))
print(f2.func2(2))
