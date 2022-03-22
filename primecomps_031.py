#!/usr/bin/env python3

import sys

for line in sys.stdin:
    # Creates list of ints from 2 to input
    nums = [int(n) for n in range(2, (int(line) + 1))]
    # Add n to primes if no number between 2 and (n // 2) + 1 divides n evenly
    primes = [n for n in nums if all(n % k != 0 for k in range(2, (n // 2) + 1))]
    print(f"Primes: {primes}")
