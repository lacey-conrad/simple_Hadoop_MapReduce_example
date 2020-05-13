#!/usr/bin/env python
import sys
from sklearn.feature_extraction import stop_words
import re


stopwords = set(stop_words.ENGLISH_STOP_WORDS)

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    line = line.lower()
    # split the line into words; splits on any whitespace
    words = line.split()
    # output tuples (word, 1) in tab-delimited format
    for word in words:
        word = re.sub(r'[^\w\s]', '', word)
        if word not in stopwords:
            print '%s\t%s' % (word, "1")
