#!/usr/bin/env python3
# imports go here
import bz2

#
# Free Coding session for 2015-03-27
# Written by Matt Warren
#

zipper = bz2.BZ2Compressor()

compressed_data = bz2.compress(b'My name is matt')
zipper.flush()
print(compressed_data)
