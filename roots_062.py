#!/usr/bin/env python3

import sys

for line in sys.stdin:
    nums = line.split()
    a = int(nums[0])
    b = int(nums[1])
    c = int(nums[2])

    D = b * b - 4 * a * c  # Calculate discriminant

    if D < 0:  # No real solutions
        print(None)
    else:
        r1 = (-b + (D ** (1 / 2))) / (2 * a)
        r2 = (-b - (D ** (1 / 2))) / (2 * a)
        print(f"r1 = {r1}, r2 = {r2}")
