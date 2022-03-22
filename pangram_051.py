#!/usr/bin/env python3

import sys

alphabet = set("abcdefghijklmnopqrstuvwxyz")

for line in sys.stdin:
    lineSet = set(line.lower())
    if len(alphabet & lineSet) == 26:  # check if intersection is == to 26
        print("pangram")
    else:
        print(f"missing {''.join(sorted(alphabet - lineSet))}")
