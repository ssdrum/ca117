#!/usr/bin/env python3

import sys

for l in sys.stdin:
    words = l.split()
    found = False
    i = 0
    while i < len(words) and not found:
        if words[i][0] == "m":
            found = True
        i += 1

    if found:
        words[i - 1] = words[i - 1].capitalize()

    print(" ".join(words))
