#!/usr/bin/env python3

def rlen(s):
    if s == "":  # part1: base case - what is the simplest string I can pass?
        return 0
    return 1 + rlen(s[1:])  # part2: reduce problem at each recursive call until it matches base case

print(rlen("abcde"))
