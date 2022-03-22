#!/usr/bin/env python3

import sys

for line in sys.stdin:
    calories = int(line)
    if calories < 400:
        print(1)
    else:
        print(int(line) // 400)
