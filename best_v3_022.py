#!/usr/bin/env python3

import sys

try:
    highest = 0
    name = ""
    with open(sys.argv[1]) as f:
        for line in f:
            try:
                tokens = line.split()
                if int(tokens[0]) > highest:
                    highest = int(tokens[0])
                    name = " ".join(tokens[1:])
            except ValueError:
                print(f"Invalid mark {tokens[0]} encountered. Skipping.")
        print(f"Best student: {name}")
        print(f"Best mark: {highest}")
except FileNotFoundError:
    print(f"The file {sys.argv[1]} could not be opened.")
