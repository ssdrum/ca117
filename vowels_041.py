#!/usr/bin/env python3

import sys

vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

def tagger(item):
    return item[1]


for c in sys.stdin.read().lower().rstrip():
    if c in vowels:
        vowels[c] += 1

padding = len(str(max(vowels.values())))

for (k, v) in sorted(vowels.items(), key=tagger, reverse=True):
    print(f"{k} : {v:{padding}}")
