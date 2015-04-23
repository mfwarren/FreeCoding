#!/usr/bin/env python3
# imports go here
import six

#
# Free Coding session for 2015-04-22
# Written by Matt Warren
#

val = b'\x01\x02'

print(val[0])
print(type(val[0]))


val = u'\x01\x02'

print(val[0])
print(type(val[0]))

sio = six.StringIO()
sio.write("HI")
sio.write(" there")
print(sio.getvalue())
