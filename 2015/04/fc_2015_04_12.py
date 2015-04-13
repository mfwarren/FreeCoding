#!/usr/bin/env python3
# imports go here
import os
from unittest.mock import MagicMock, call

#
# Free Coding session for 2015-04-12
# Written by Matt Warren
#


class Foo(object):
    def set_gpio(self):
        os.system('/usr/bin/gpio +P13')
        return os.system('/usr/bin/gpio +P12')

thing = Foo()
pre_mock = thing.set_gpio
thing.set_gpio = MagicMock(return_value=2)
print(thing.set_gpio(1, 2, 3))

try:
    thing.set_gpio.assert_called_with(1, 2, 5)
except AssertionError:
    pass

thing.set_gpio = pre_mock


def test():
    os.system = MagicMock(return_value="ran os command")
    assert thing.set_gpio() == 'ran os command'
    print(os.system.mock_calls)
    os.system.assert_has_calls([call('/usr/bin/gpio +P13'), call('/usr/bin/gpio +P12')])
    print("AWESOME")

test()
