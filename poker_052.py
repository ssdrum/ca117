#!/usr/bin/env python3

hand = input().split()
count = {}

def tagger(item):
    return item[1]


for c in hand:
    strength = c[0]
    if strength in count:
        count[strength] += 1
    else:
        count[strength] = 1

print(max(count.items(), key=tagger)[1])
