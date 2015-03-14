#!/usr/bin/env python3
# imports go here

#
# Free Coding session for 2015-03-13
# Written by Matt Warren
#


class Example(object):
    def name(self):
        return 'name'
    print(type(name))

print(type(Example.name))  # this is different in python 2/3

measures = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]

# bad examples:
# print([beat for beat in measure for measure in measures])
print([beat for beat in [measure for measure in measures]])
print([[beat for beat in measure] for measure in measures])
print([beat for measure in measures for beat in measure])
# print([[beat for measure in measures] for beat in measure])
# print([beat for measure in [measures for beat in measure]])
print([measure for measure in measures])

# much easier to understand:
flat = []
for measure in measures:
    flat.extend(measure)
print(flat)
