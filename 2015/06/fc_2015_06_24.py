#!/usr/bin/env python3
# imports go here

#
# Free Coding session for 2015-06-24
# Written by Matt Warren
#

names = ["Matt", "Chris", "Heather"]

up_names = [n.upper() for n in names]
print(up_names)

up_names.sort()
print(up_names)

lengths = [len(n) for n in names]
len_dict = {n: len(n) for n in names}
print(len_dict)

names.append("John")

names.append("Matt")

print(names)
name_set = set(names)
name_frozenset = frozenset(names)
print(name_set)
print(name_frozenset)

name_set.add("Jill")
print(name_set)
try:
    name_frozenset.add("Bob")
except AttributeError:
    pass
