#!/usr/bin/env python3

import sys

for l in sys.stdin:
    words = l.split()
    words[0] = words[0].lower()
    words[1] = words[1].lower()
    s = words[1]

    for c in words[0]:
        if c in words[1]:
            s = s.replace(c, "")

    if len(s) == len(words[1]) - len(words[0]):
        print(True)
    else:
        print(False)
