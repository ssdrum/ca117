#!/usr/bin/env python3

import sys

lines = sys.stdin.read().rstrip().split("\n")
liters = int(lines[0])
buckets = []

for n in lines[1].split():
    buckets.append(int(n))

i = 0
while 0 < liters and i < len(buckets):
    liters -= buckets[i]
    i += 1

if liters < 0:
    print(i - 1)
else:
    print(i)
