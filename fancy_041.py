#!/usr/bin/env python3

import sys

contacts = {}

with open(sys.argv[1]) as f:
    for line in f:
        [name, num, email] = line.split()
        contacts[name] = (num, email)

for line in sys.stdin:
    try:
        print(f"Name: {line.strip()}")
        print(f"Phone: {contacts[line.strip()][0]}")
        print(f"Email: {contacts[line.strip()][1]}")
    except KeyError:
        print("No such contact")
