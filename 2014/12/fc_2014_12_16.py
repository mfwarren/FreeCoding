#!/usr/bin/env python3
# imports go here
import re
import string
from collections import Counter

#
# Free Coding session for 2014-12-16
# Written by Matt Warren
#


def remove_punctuation(s):
    exclude = set(string.punctuation)
    return ''.join(ch for ch in s if ch not in exclude)


def tokenize(text):
    text = remove_punctuation(text)
    text = text.lower()
    return re.split("\W+", text)


def count_words(words):
    wc = Counter()
    for word in words:
        wc[word] += 1
    return wc


s = "Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design."
print(count_words(tokenize(s)))
