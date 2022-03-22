#!/usr/bin/env python3

def swap_unique_keys_values(d):
    swapd = {}
    vals_count = {}
    for v in d.values():
        if v in vals_count:
            vals_count[v] += 1
        else:
            vals_count[v] = 1

    for val in vals_count:
        if vals_count[val] == 1:
            for k, v in d.items():
                if v == val:
                    swapd[v] = k

    return swapd
