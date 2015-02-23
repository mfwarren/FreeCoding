#!/usr/bin/env python3
# imports go here

#
# Free Coding session for 2015-02-22
# Written by Matt Warren
#


def decorator(wrapped_function):
    def _wrapper(*args, **kwargs):
        print("before")
        result = wrapped_function(*args, **kwargs)
        print("after")
        return result
    return _wrapper


@decorator
def f(s):
    print(s)


def decorator_2(arg1, arg2):
    def _outer_wrapper(wrapped_function):
        def _wrapper(*args, **kwargs):
            print(arg1)
            result = wrapped_function(*args, **kwargs)
            print(arg2)
            return result
        return _wrapper
    return _outer_wrapper


@decorator_2("start", "end")
def g(s):
    print(s)

if __name__ == '__main__':
    f("HELLO")
    g("I WIN!")
