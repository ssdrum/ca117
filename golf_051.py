#!/usr/bin/env python3

import sys

# returns tot number of shots, or -1 if a ValueError occurs
def calcShots(nums):
    try:
        tot = 0
        for n in nums:
            tot += int(n)
        return tot
    except ValueError:
        return -1


def tagger(item):
    return item[1]


results = {}

for line in sys.stdin:
    tokens = line.split()
    totShots = calcShots(tokens[-3:])
    name = " ".join(tokens[:-3])
    results[name] = totShots

disqual = []
for k, v in sorted(results.items(), key=tagger):
    if v == -1:
        disqual.append(k)
    else:
        print(f"{k}: {v}")

if len(disqual) > 0:
    print(f"Disqualified: {', '.join(disqual)}")
