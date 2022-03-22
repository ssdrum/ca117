#!/usr/bin/env python3

import sys

def isPalindrome(s):
    formatS = ""
    for c in s:
        if c.isalnum():
            formatS += c.lower()

    i = 0
    while i < len(formatS) and formatS[i] == formatS[len(formatS) - 1 - i]:
        i += 1

    if i == len(formatS):
        return True
    else:
        return False


for line in sys.stdin:
    print(isPalindrome(line))
