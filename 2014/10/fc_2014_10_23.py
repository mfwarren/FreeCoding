#!/usr/bin/env python
#imports go here

#
# Free Coding session for 2014-10-23
# Written by Matt Warren
#

# Bunch class is a neat hack to give .attribute access on dictionary
class Bunch(dict):
    def __init__(self, *args, **kwargs):
        super(Bunch, self).__init__(*args, **kwargs)
        self.__dict__ = self

if __name__=='__main__':
    b = Bunch(name="Matt", age=33)
    print b
    print b.name
    print b['age']
    b.last_name = 'Warren'
    print b.last_name
