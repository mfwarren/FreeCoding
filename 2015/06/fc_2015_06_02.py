#!/usr/bin/env python3
# imports go here
import math

#
# Free Coding session for 2015-06-02
# Written by Matt Warren
#

def fun_with_logs():
    a = 1234
    b = 65473
    a_x_b = a * b

    print(a_x_b)
    print(math.exp(math.log(a) + math.log(b)))

    # 6th root
    root = math.exp(1/6 * math.log(b))
    print(root)
    print(root**6)

if __name__ == '__main__':
    fun_with_logs()
