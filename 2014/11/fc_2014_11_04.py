#!/usr/bin/env python
# imports go here
from sh import ffmpeg, ffmpeg2theora
import sys

#
# Free Coding session for 2014-11-04
# Written by Matt Warren
#


def convert_mp4_to_web(input_filename):
    # given input mp4 convert to webm, flash, and ogv
    prefix = input_filename.split('.')[-2]
    ffmpeg(i=input_filename, f='webm', vcodec='libvpx', acodec='libvorbis', ab=128000, crf=22, s='640x360', out='%s.webm' % prefix)
    ffmpeg2theora(input_filename, x=640, y=360, videoquality=5, audioquality=0, frontend=True, o='%s.ogv' % prefix)
    ffmpeg("-i", input_filename, "-c:v", "flv", "-c:a", "mp3", "-ar", "44100", "%s.flv" % prefix)

if __name__ == '__main__':
    convert_mp4_to_web(sys.argv[1])
