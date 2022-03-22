#!/usr/bin/env python3

import sys

num1 = []
num2 = []

with open(sys.argv[1]) as f:
    for line in f:
        num1.append(line.strip())

with open(sys.argv[2]) as f:
    for line in f:
        num2.append(line.strip())

for i in range(len(num1) * 2):
    if i % 2 == 0:
        print(num1[i // 2])
    else:
        print(num2[i // 2])
