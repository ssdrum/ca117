#!/usr/bin/env python3

def sumup(n):
    if n == 0:
        return 0
    else:
        return n + sumup(n - 1)


def main():
    pass


if __name__ == "__main__":
    main()
