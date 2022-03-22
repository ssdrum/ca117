#!/usr/bin/env python3

import sys

vowels = "aeiouy"
es = ["ch", "sh", "x", "s", "z"]

for noun in sys.stdin:
    noun = noun.strip()
    if noun[-1:] in es or noun[-2:] in es:
        print(f"{noun}es")
    elif noun[-2] not in vowels and noun[-1] == "y":
        print(f"{noun[:-1]}ies")
    elif noun[-1] == "f":
        print(f"{noun[:-1]}ves")
    elif noun[-2:] == "fe":
        print(f"{noun[:-2]}ves")
    elif noun[-1] == "o":
        print(f"{noun}es")
    else:
        print(f"{noun}s")
