#!/usr/bin/env python3

import sys

for l in sys.stdin:
    s = l.rstrip()
    if len(s) % 2 == 1:
        print(s[len(s) // 2])
    else:
        print("No middle character!")
