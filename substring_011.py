#!/usr/bin/env python3

import sys

for l in sys.stdin:
    words = l.split()
    [left, right] = words
    if left.lower() in right.lower():
        print(True)
    else:
        print(False)
