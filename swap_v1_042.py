#!/usr/bin/env python3

def swap_keys_values(d):
    swapd = {}
    for k, v in d.items():
        swapd[v] = k
    return swapd
