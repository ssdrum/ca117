#!/usr/bin/env python3

import sys

try:
    highest = 0
    names = []
    with open(sys.argv[1]) as f:
        for line in f:
            try:
                tokens = line.split()
                if int(tokens[0]) > highest:
                    highest = int(tokens[0])
                    names = [" ".join(tokens[1:])]
                elif int(tokens[0]) == highest:
                    names.append(" ".join(tokens[1:]))
            except ValueError:
                print(f"Invalid mark {tokens[0]} encountered. Skipping.")
        print(f"Best student(s): {', '.join(names)}")
        print(f"Best mark: {highest}")
except FileNotFoundError:
    print(f"The file {sys.argv[1]} could not be opened.")
