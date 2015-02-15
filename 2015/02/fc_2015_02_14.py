#!/usr/bin/env python3
# imports go here

#
# Free Coding session for 2015-02-14
# Written by Matt Warren
#


class Attr:
    def __getattr__(self, key):
        if key == 'matt':
            return 'warren'
        else:
            raise AttributeError


class Attribute:
    def __getattribute__(self, key):
        if key == 'matt':
            return 'warren'
        else:
            raise AttributeError

if __name__ == '__main__':
    m = Attr()
    print(m.matt)
    m.matt = 'missing'
    print(m.matt)

    m = Attribute()
    print(m.matt)
    m.matt = 'missing'
    print(m.matt)
