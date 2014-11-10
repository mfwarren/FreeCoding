#!/usr/bin/env python
# imports go here

#
# Free Coding session for 2014-11-09
# Written by Matt Warren
#


def is_balanced(s):
    count = 0
    for c in s:
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
            if count < 0:
                return False
    if count == 0:
        return True
    return False


s = '(()(())()()()'
assert(not is_balanced(s))


assert(is_balanced('()(())()()()'))
assert(is_balanced('()((((((((()))))))))()()()'))
assert(is_balanced('()(((()()()()()())))()()()'))
assert(is_balanced('(asdf)()'))
