#!/usr/bin/env python3

import sys

def main():
    names = [name.rstrip() for name in sys.stdin]

    first_half = []
    second_half = []
    for i, n in enumerate(names):
        if i % 2 == 0:
            first_half.append(n)
        else:
            second_half.append(n)
    second_half.reverse()
    symm_names = first_half + second_half

    for n in symm_names:
        print(n)


if __name__ == "__main__":
    main()
