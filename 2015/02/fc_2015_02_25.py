#!/usr/bin/env python3
# imports go here
import warnings

#
# Free Coding session for 2015-02-25
# Written by Matt Warren
#


def obsolete():
    warnings.warn("This is obsolete")
    return None


def deprecated_fn():
    warnings.warn('deprecated', DeprecationWarning)
    return None

if __name__ == '__main__':
    obsolete()  # will print out warnings

    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        obsolete()  # warnings supressed

    deprecated_fn()
