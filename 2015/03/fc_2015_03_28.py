#!/usr/bin/env python3
# imports go here
import bz2
import gzip
import zlib
import lzma
import cProfile
import pstats
from os import urandom

#
# Free Coding session for 2015-03-28
# Written by Matt Warren
#
if __name__ == '__main__':
    data = b''.join([urandom(100) for i in range(1000000)])
    profile = cProfile.Profile()
    profile.enable()
    compressed_data = bz2.compress(data)
    compressed_data = gzip.compress(data)
    compressed_data = zlib.compress(data)
    compressed_data = lzma.compress(data)
    profile.disable()
    ps = pstats.Stats(profile)
    ps.print_stats()
