#!/usr/bin/env python3

def fact(n):
    if n == 1:
        return n
    else:
        return n * (fact(n - 1))

print(fact(4))
