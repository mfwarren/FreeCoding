#!/usr/bin/env python3
# imports go here

#
# Free Coding session for 2015-03-02
# Written by Matt Warren
#


class SimpleClass:
    def main(self):
        return "HI"
    def main2(self):
        return "HELLO AGAIN"

if __name__ == '__main__':
    sc = SimpleClass()
    assert(sc.main.__name__ == 'main')

    fn = getattr(sc, 'main')
    assert(fn() == 'HI')

    fn = getattr(sc, 'main', sc.main2)
    assert(fn() == 'HI')

    fn = getattr(sc, 'main3', sc.main2)
    assert(fn() == 'HELLO AGAIN')

    setattr(sc, 'main3', fn)
    fn = getattr(sc, 'main3', sc.main2)
    assert(fn() == 'HELLO AGAIN')
    assert(sc.main3() == 'HELLO AGAIN')
