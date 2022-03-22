#!/usr/bin/env python3

import sys

nums = [1, 12 ,33550336, 10, 28]

def sum_factors(n):
    factors = [i for i in range(1, n // 2 + 1) if n % i == 0]
    return sum(factors)


def is_perfect(n):
    return True if n == sum_factors(n) else False


for n in nums:
    print(is_perfect(int(n)))
