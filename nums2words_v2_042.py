#!/usr/bin/env python3

import sys

numbers = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten"
}

for line in sys.stdin:
    output = ""
    nums = line.split()
    for n in nums:
        try:
            output += numbers[int(n)] + " "
        except (KeyError, ValueError):
            output += "unknown "
    print(output[:-1])
