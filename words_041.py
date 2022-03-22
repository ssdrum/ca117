#!/usr/bin/env python3

import sys

words = {}

for w in sys.stdin.read().rstrip().split():
    w = w.lower().strip()
    formw = ""
    for c in w:
        if c.isalpha() or c == "'":
            formw += c
    if formw in words:
        words[formw] += 1
    else:
        words[formw] = 1

for (k, v) in sorted(words.items()):
    print(f"{k} : {v}")
