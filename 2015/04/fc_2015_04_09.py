#!/usr/bin/env python3
# imports go here
import threading

#
# Free Coding session for 2015-04-09
# Written by Matt Warren
#

data = threading.local()


def message():
    print(data.name)


class Foo(threading.Thread):
    def run(self):
        data.name = self.getName()
        message()

if __name__ == '__main__':
    f = Foo()
    f2 = Foo()
    f.start()
    f2.start()
