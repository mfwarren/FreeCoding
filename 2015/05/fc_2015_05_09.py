#!/usr/bin/env python3
# imports go here
import re

#
# Free Coding session for 2015-05-09
# Written by Matt Warren
#


paragraph = "The practice of writing paragraphs is essential to good writing. Paragraphs help to break up large chunks of text and makes the content easier for readers to digest. However, knowing how to write a good, well-structured paragraph can be little tricky. Read the guidelines below and learn how to take your paragraph writing skills from good to great!"

match = re.search('paragraph', paragraph)
print(match.group(0))
