#!/usr/bin/env python3
# imports go here

#
# Free Coding session for 2015-03-21
# Written by Matt Warren
#


def manipulate(func):
    def inner(s):
        return func(s)
    return inner


class Special(object):
    def __init__(self, str_to_append):
        self.str_to_append = str_to_append

    def __call__(self, value):
        return value + self.str_to_append


if __name__ == '__main__':
    appender = Special(' from matt')
    manipulator = manipulate(appender)

    print(manipulator('hello'))
