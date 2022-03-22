#!/usr/bin/env python3

import sys

for line in sys.stdin:
    nums = [int(n) for n in range(1, int(line) + 1)]
    output = ["X" if n % 3 == 0 else n for n in nums]
    print(f"Multiples of 3 replaced: {output}")
