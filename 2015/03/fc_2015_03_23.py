#!/usr/bin/env python3
# imports go here
import json

#
# Free Coding session for 2015-03-23
# Written by Matt Warren
#


class JsonSerializableMixin(object):
    def toJson(self):
        return json.dumps(self.__dict__)


class Simple(JsonSerializableMixin):
    def __init__(self, name):
        self.name = name


class AnotherJsonSerializer(object):
    def __init__(self, *args):
        self.args = args

    def serialize(self):
        return json.dumps({'args': self.args})


class AnotherSimple(AnotherJsonSerializer):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

if __name__ == '__main__':
    s = Simple('matt')
    print(s.toJson())

    s = AnotherSimple('matt')
    print(s.serialize())
