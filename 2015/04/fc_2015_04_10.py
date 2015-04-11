#!/usr/bin/env python3
# imports go here

#
# Free Coding session for 2015-04-10
# Written by Matt Warren
#


def fo():
    print("H")
    a = "asdf"
    print(a[::-1])
    print(a.upper())


class Mine(object):
    def __init__(self):
        super().__init__()
        self.something = "the key"

    def run(self):
        print(self.something)
        for i in range(100):
            print(i)
        for i in range(100, 1, -1):
            print(i)


if __name__ == "__main__":
    fo()
    f = Mine()
    f.run()
