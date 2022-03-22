#!/usr/bin/env python3

import sys

for l in sys.stdin:
    nums = False
    upper = False
    lower = False
    special = False

    for c in l.rstrip():
        if c.isnumeric():
            nums = True
        elif c.isupper():
            upper = True
        elif c.islower():
            lower = True
        else:
            special = True

    print(nums + upper + lower + special)
