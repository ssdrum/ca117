#!/usr/bin/env python3

def printn(n):
    if n == 6:
        return
    print(n)
    printn(n + 1)
    return

printn(1)
