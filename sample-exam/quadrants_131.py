#!/usr/bin/env python3

import sys

def calc_quadrant(x, y):
    if x > 0:
        if y > 0:
            return 1
        else:
            return 2
    else:
        if y > 0:
            return 4
        else:
            return 3


def main():
    for line in sys.stdin:
        x, y = line.split()
        print(calc_quadrant(int(x), int(y)))


if __name__ == "__main__":
    main()
