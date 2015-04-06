#!/usr/bin/env python3
# imports go here
import pytest

#
# Free Coding session for 2015-04-05
# Written by Matt Warren
#


class Foo(object):
    def __init__(self, name):
        self.name = name
    def delete(self):
        self.name = ''

def test_something():
    assert True == False


class TestGroup:

    @pytest.fixture
    def info(self):
        return 'INFO'

    @pytest.fixture
    def myfoo(self, request):
        f = Foo('Matt')
        def cleanup():
            f.delete()
        request.addfinalizer(cleanup)
        return f

    def test_something_else(self, info):
        assert info == 'INFO'
        assert 0

    def test_foo(self, myfoo):
        assert myfoo.name == 'Matt'


if __name__ == '__main__':
    pytest.main(__file__)
