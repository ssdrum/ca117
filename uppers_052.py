#!/usr/bin/env python3

import sys

# save positions of uppercase substrings in list of touples (start, end)
for line in sys.stdin:
    substrings = []
    i = 0
    while i < len(line.rstrip()):
        if line[i].isupper():
            j = i + 1
            while line[j].isupper() and j < len(line.rstrip()):
                j += 1
            substrings.append((i, j))
            i = j + 1
        else:
            i += 1

    # find touple with largest difference (end - start)
    maxDiff = 0
    longest = ()
    i = 0
    while i < len(substrings):
        if substrings[i][1] - substrings[i][0] > maxDiff:
            longest = substrings[i]
        i += 1

    # print that substring
    print(line[longest[0]:longest[1]])
