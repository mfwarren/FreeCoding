#!/usr/bin/env python3
# imports go here

#
# Free Coding session for 2015-03-14
# Written by Matt Warren
#


if __name__ == '__main__':
    uni = 'ßœ∑çß†¥å'  # strings are unicode characters without an encoding yet
    print(uni)

    to_binary = uni.encode('utf-8')  # translating to binary requires specifing the encoding for the characters to use
    print(type(to_binary))  # `bytes`

    print(to_binary)  # \x...

    # back to unicode
    to_unicode = to_binary.decode('utf-8')
    print(to_unicode)

    # attempt to decode with encodding that can't handle unicode chars
    try:
        to_ascii = to_binary.decode('ascii')
    except UnicodeDecodeError as e:
        print('failed to decode the bytes into ascii :(')
