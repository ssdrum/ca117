#!/usr/bin/env python3

import sys

def chop(s):
    return s[1:-1]


for l in sys.stdin:
    chopped = chop(l.rstrip())
    if len(chopped) > 0:
        print(chopped)
