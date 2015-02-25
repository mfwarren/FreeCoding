#!/usr/bin/env python3
# imports go here

#
# Free Coding session for 2015-02-24
# Written by Matt Warren
#


def bad_outter():
    a = 0

    def inner():
        a += 1
        return a
    inner()


def good_outter():
    a = 0

    def inner():
        nonlocal a
        a += 1
        return a
    return inner()


if __name__ == '__main__':
    try:
        bad_outter()
    except UnboundLocalError as e:
        print("bad_outter failed because variable was not scoped correctly")

    print(good_outter())
