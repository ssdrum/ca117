#!/usr/bin/env python3

import sys

text = sys.stdin.read().strip()
formatText = ""
uniques = {}
tot = 0

for c in text:
    if c.isalnum() or c == " " or c == "\n":
        formatText += c.lower()

words = formatText.split()

for w in words:
    if w not in uniques:
        uniques[w] = True
        tot += 1

print(tot)
