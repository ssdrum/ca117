#!/usr/bin/env python3

import sys

vowels = {"a", "e", "i", "o", "u"}

def decode(text):
    output = ""
    i = 0
    while i < len(text):
        output += text[i]
        if text[i] in vowels:
            i += 3
        else:
            i += 1

    return output


def main():
    for line in sys.stdin:
        print(decode(line.rstrip()))


if __name__ == "__main__":
    main()
