#!/usr/bin/env python3
# imports go here

#
# Free Coding session for 2015-05-16
# Copyright (c) 2014 Copyright Holder All Rights Reserved.
# Written by Matt Warren
#

lorem = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."


class MyClass(object):
    """docstring for MyClass"""
    def __init__(self, arg):
        super(MyClass, self).__init__()
        self.arg = arg

    def awesome(self):
        for word in lorem.split(" "):
            pass
        try:
            pass
        except Exception as e:
            raise
        import pdb; pdb.set_trace()

        print("implment stuff")

        self.arg

    def __repr__(self):
        return "<MyClass>"

def fake():
    doc = "The fake property."
    def fget(self):
        return self._fake
    def fset(self, value):
        self._fake = value
    def fdel(self):
        del self._fake
    return locals()
fake = property(**fake())

def main():
    mc = MyClass('secret arg')
    mc.awesome()

    def inner():
        mc.awesome()

    return inner

if __name__ == '__main__':
    f = main()
    f()
    print(dir(fake))
