#!/usr/bin/env python3
# imports go here
import sys

#
# Free Coding session for 2015-02-03
# Written by Matt Warren
#


if __name__ == '__main__':
    # comparing strings
    assert('\\r' == r'\r')

    print(r"'\\r' == r'\r'")

    print("b'' uses %d bytes" % sys.getsizeof(b''))
    print("b'hi' uses %d bytes" % sys.getsizeof(b'hi'))
    print("b'hello' uses %d bytes" % sys.getsizeof(b'hello'))

    print("u'' uses %d bytes" % sys.getsizeof(u''))
    print("u'hi' uses %d bytes" % sys.getsizeof(u'hi'))
    print("u'hello' uses %d bytes" % sys.getsizeof(u'hello'))
