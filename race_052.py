#!/usr/bin/env python3

import sys

best = ["", 10000]

for line in sys.stdin:
    tokens = line.split()
    name = tokens[0]
    for t in tokens[1:]:
        [mins, secs] = t.split(":")
        try:
            totTime = int(mins) * 60 + int(secs)
            if totTime < best[1]:
                best = [name, totTime]
        except ValueError:
            pass

print(f"{best[0]} : {best[1] // 60}:{best[1] % 60}")
