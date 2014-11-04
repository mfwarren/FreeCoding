#!/usr/bin/env python
#imports go here
import random
from collections import Counter

#
# Free Coding session for 2014-10-24
# Written by Matt Warren
#

def split(primary_percentage=50):
    def innersplit(fn):
        split.f2 = None
        def inner(*args, **kwargs):
            if random.randint(0,100) < primary_percentage:
                return fn(*args, **kwargs)
            else:
                return split.f2(*args, **kwargs)
        def B(fn2):
            split.f2 = fn2
        inner.B = B
        return inner
    return innersplit

class Interesting:
    @split(primary_percentage=80)
    def A(self):
        return "A"
    @A.B
    def B(self):
        return "B"

if __name__=='__main__':
    cnt = Counter()
    interesting = Interesting()
    for i in xrange(100):
        res = interesting.A()
        cnt[res] += 1
    print cnt
