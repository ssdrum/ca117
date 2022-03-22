#!/usr/bin/env python3

import sys

for l in sys.stdin:
    i = 0
    while i < len(l) and not l[i].isnumeric():
        i += 1
    a = l[:i].split(".")
    name = a[0].capitalize()
    surname = a[1].capitalize()
    print(f"{name} {surname}")
