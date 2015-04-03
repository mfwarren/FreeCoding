#!/usr/bin/env python3
# imports go here

#
# Free Coding session for 2015-04-02
# Written by Matt Warren
#


class MyClass(object):

    def __init__(self):
        self.meta = self.Meta()

    class Meta:
        CONSTANT = 'HELLO'

    def do_something(self):
        print(self.meta.CONSTANT)


class MySubclass(MyClass):

    class Meta:
        CONSTANT = 'MATT IS COOL'

if __name__ == '__main__':
    mc = MyClass()
    mc.do_something()

    msc = MySubclass()
    msc.do_something()
