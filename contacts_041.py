#!/usr/bin/env python3

import sys

contacts = {}

with open(sys.argv[1]) as f:
    for line in f:
        [name, num] = line.split()
        contacts[name] = num

for line in sys.stdin:
    try:
        print(f"Name: {line.strip()}")
        print(f"Phone: {contacts[line.strip()]}")
    except KeyError:
        print("No such contact")
