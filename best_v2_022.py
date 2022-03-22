#!/usr/bin/env python3

import sys

try:
    highest = 0
    name = ""
    with open(sys.argv[1]) as f:
        try:
            for line in f:
                tokens = line.split()
                if int(tokens[0]) > highest:
                    highest = int(tokens[0])
                    name = " ".join(tokens[1:])
            print(f"Best student: {name}")
            print(f"Best mark: {highest}")
        except ValueError:
            print(f"Invalid mark {tokens[0]} encountered. Exiting.")
except FileNotFoundError:
    print(f"The file {sys.argv[1]} could not be opened.")
