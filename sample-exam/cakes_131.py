#/usr/bin/env python3

import sys

for line in sys.stdin:
    prices = [int(price) for price in line.split()]
    prices.sort()
    disconted = len(prices) // 3
    print(sum(prices[disconted:]))
