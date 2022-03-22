#!/usr/bin/env python3

water = int(input())
buckets = [int(n) for n in input().split()]

i = 0
while i < len(buckets) and water > 0:
    water -= buckets[i]
    i += 1

print(i - 1)
