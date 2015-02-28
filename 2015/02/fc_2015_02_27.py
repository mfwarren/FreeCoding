#!/usr/bin/env python3
# imports go here
import inspect

#
# Free Coding session for 2015-02-27
# Written by Matt Warren
#


def f(arg):
    print(arg)


class Foo:
    """
    sample comment
    """
    def method(self, arg):
        print(arg)


if __name__ == '__main__':
    print("f is method? %s" % inspect.ismethod(f))
    print("f is function? %s" % inspect.isfunction(f))
    print("f signature %s" % inspect.signature(f))
    print("Foo is class? %s" % inspect.isclass(Foo))
    foo = Foo()
    print("foo is class? %s" % inspect.isclass(foo))
    print("foo is method? %s" % inspect.ismethod(foo.method))

    print("members of foo %s" % inspect.getmembers(foo))

    print(inspect.getdoc(Foo))

    frame = inspect.currentframe()
    print(inspect.getframeinfo(frame))
