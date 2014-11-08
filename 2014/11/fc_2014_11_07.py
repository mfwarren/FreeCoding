#!/usr/bin/env python
# imports go here
import re

#
# Free Coding session for 2014-11-07
# Written by Matt Warren
#


s = 'asdf'

print re.sub('a', '*', s)

m = re.match('a', s)
print 'match grouop 0:', m.group(0)

m = re.match('s', s)
assert(m, None)  # match only finds fromt he beginning of the string
# print 'match grouop 0:', m.group(0)

m = re.search('s', s)
print 'searching for s', m.group(0)  # search will find stuff in the string

print '-- find iter letters between a-f'
for c in re.finditer('[a-f]', s):
    print c.group(0)

m = re.search('([a-f])', s)  # only one group per match
print m.groups()  # will show ('a',)

m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
print m.group(0)

m = re.match(r"(\w+) (\w+)", " Isaac Newton, physicist")  # leading space breaks this match
assert(m, None)

print re.findall('([a-f])', s)

m = re.search('(?P<letter>[a-f])', s)
print m.groupdict()
