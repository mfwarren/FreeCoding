#!/usr/bin/env python
#imports go here
from collections import *

#
# Free Coding session for 2014-10-22
# Written by Matt Warren
#
words = ['orange', 'red', 'blue', 'red', 'grey', 'pink', 'blue', 'red']
if __name__=='__main__':
    cnt = Counter()
    for word in words:
        cnt[word] += 1
    print cnt
    print cnt.most_common(2)
    print cnt.values()


    numbers = range(len(words))
    cnt2 = Counter(dict(zip(words, numbers)))
    print cnt2

    cnt.subtract(cnt2)
    print cnt

    d = deque()
    d.extend([1,2,3,4])
    d.append(5)
    d.extendleft([0, -1, -2, -3])
    d.appendleft(-4)
    d.reverse()
    print d

    dd = defaultdict(int)
    for word in words:
        dd[word] += 1
    print dd

    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1, 2)
    print p
    print p.x, p.y
