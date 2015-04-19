#!/usr/bin/env python3
# imports go here

#
# Free Coding session for 2015-04-18
# Written by Matt Warren
#


class Foo(object):
    nice_level = "HI THERE"

    def __init__(self, name):
        self.name = name

    def p(self):
        return self.nice_level

    def q(self):
        return Foo.nice_level


def foo():
    f = Foo("matt")
    print(f.p())
    print(f.q())
    print(dir(f))
    print(dir(Foo))

    print([item for item in dir(f) if item not in dir(Foo)])
    print([item for item in dir(Foo) if item not in dir(f)])

if __name__ == '__main__':
    foo()
