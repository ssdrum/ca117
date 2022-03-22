#!/usr/bin/env python3

import sys

censWords = []
censText = ""

with open(sys.argv[1]) as f:
    censWords = [w.strip() for w in f.readlines()]

text = sys.stdin.read().strip()
lowerText = text.lower()

for w in censWords:
    lowerText = lowerText.replace(w, "@" * len(w))

for i, c in enumerate(lowerText):
    if c == "@":
        censText += "@"
    else:
        censText += text[i]

print(censText)
