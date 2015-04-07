#!/usr/bin/env python3
# imports go here
import pytest

#
# Free Coding session for 2015-04-06
# Written by Matt Warren
#

class Stuff(object):
    def __init__(self, num):
        self.num = num

@pytest.fixture(params=[0, 1, 2], ids=['asdf', 'dd', 'as'])
def a(request):
    return Stuff(request.param)

def test_a(a):
    assert isinstance(a, Stuff)


if __name__ == '__main__':
    pytest.main(__file__)
