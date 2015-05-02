#!/usr/bin/env python3
# imports go here

#
# Free Coding session for 2015-05-01
# Written by Matt Warren
#

class ASingleton:
    class __ActualSingleton:
        def __init__(self, arg):
            self.val = arg

        def __str__(self):
            return repr(self) + self.val
    instance = None

    def __init__(self, arg):
        if not ASingleton.instance:
            ASingleton.instance = ASingleton.__ActualSingleton(arg)
        else:
            ASingleton.instance.val = arg

    def __getattr__(self, name):
        return getattr(self.instance, name)


if __name__ == '__main__':
    a = ASingleton('a')
    b = ASingleton('b')
    assert a != b
    assert a.instance == b.instance
