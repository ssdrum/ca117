#!/usr/bin/env python3

import sys

tokens = sys.stdin.readline().split()
nums = [int(i) for i in tokens]

nums.sort()

abc = {
    "a": nums[0],
    "b": nums[1],
    "c": nums[2]
}

order = sys.stdin.readline().strip().lower()
output = ""

for c in order:
    output += f"{abc[c]} "

print(output[:-1])
