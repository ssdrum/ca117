#!/usr/bin/env python3

nums = [int(n) for n in input().split()]
rooms = {}

for n in range(1, nums[0]):
    if n not in nums:
        rooms[n] = True

if len(rooms) > 0:
    print(min(rooms.keys()))
else:
    print("no room")
