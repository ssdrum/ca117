#!/usr/bin/env python3

import sys

text = sys.stdin.readlines()
padding = 0

for line in text:
    if len(line) > padding:
        padding = len(line) - 1

for line in text:
    line = line.strip()
    print(f"{line:^{padding}}")
