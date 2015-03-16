#!/usr/bin/env python3
# imports go here

#
# Free Coding session for 2015-03-15
# Written by Matt Warren
#


def simple_generator(count):
    for i in range(count):
        yield i


class Ranger(object):
    # creating an iterable class like this because I want to use it
    # multiple times in the same function (evalutate) without either exhausting
    # the generator or having to expand into an array.
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        for i in range(self.count):
            yield i


def evaluate(arr):
    if iter(arr) is iter(arr):
        raise ValueError("invalid arguments")
    total = float(sum(arr))
    result = []
    for i in arr:
        result.append(i / total)
    return result

if __name__ == '__main__':
    r = Ranger(10)
    print(evaluate(r))

    a_range = range(10)
    print(type(a_range))
    print(evaluate(a_range))

    try:
        print(evaluate(simple_generator(10)))
    except ValueError:
        print("can't use a simple generator like this")
