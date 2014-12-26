#!/usr/bin/env python3
# imports go here
import timeit
import string


#
# Free Coding session for 2014-12-26
# Written by Matt Warren
#

fmt = 'Hello {}!'.format
tmplt = string.Template('Hello $name!')


def format_new_string(name):
    return 'Hello {}!'.format(name)


def format_exiting_string(name):
    return fmt(name)


def template_new(name):
    t = string.Template('Hello $name!')
    return t.substitute(name=name)


def template_existing(name):
    return tmplt.substitute(name=name)


def percent_new(name):
    return 'Hello %s!' % name


if __name__ == '__main__':
    v1 = timeit.timeit('format_new_string("Matt")', setup="from __main__ import format_new_string")
    v2 = timeit.timeit('format_exiting_string("Matt")', setup="from __main__ import format_exiting_string")
    v3 = timeit.timeit('template_new("Matt")', setup="from __main__ import template_new")
    v4 = timeit.timeit('template_existing("Matt")', setup="from __main__ import template_existing, tmplt")
    v5 = timeit.timeit('percent_new("Matt")', setup="from __main__ import percent_new")

    print('format_new_string', v1)
    print('format_existing_string', v2)
    print('template_new', v3)
    print('template_existing', v4)
    print('percent_new', v5)
