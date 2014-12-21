#!/usr/bin/env python3
# imports go here
import json


#
# Free Coding session for 2014-12-21
# Written by Matt Warren
#


def make_a_class(classname, **kwargs):
    return type(classname, (object,), dict(**kwargs))


definition = """{"classname": "Gold",
"is_shiny": true,
"values": [1088, 1100, 1375]}
"""

if __name__ == '__main__':
    runtime_class = make_a_class('Matt', about='is cool')

    # instantiate new class
    matt = runtime_class()
    print(matt.about)

    new_class = make_a_class(**json.loads(definition))
    k = new_class()
    if 'is_shiny' in dir(k):
        print(k.is_shiny)
    if 'values' in dir(k):
        print(k.values)
