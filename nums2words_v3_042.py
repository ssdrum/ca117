#!/usr/bin/env python3

import sys

mapping = {}

with open(sys.argv[1]) as f:
    lines = f.readlines()
    for i, l in enumerate(lines):
        mapping[i] = l.split()[1]

for line in sys.stdin:
    output = ""
    for n in line.split():
        output += mapping[int(n)] + " "
    print(output[:-1])
