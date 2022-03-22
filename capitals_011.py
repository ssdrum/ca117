#!/usr/bin/env python3

import sys

def capital(s):
    if len(s) > 1:
        first = s[0].capitalize()
        last = s[-1].capitalize()
        return f"{first}{s[1:-1]}{last}"


for l in sys.stdin:
    s = capital(l.rstrip())
    if s:
        print(s)
