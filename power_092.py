#!/usr/bin/env python3

def power(m, n):
    if n == 0:
        return 1
    else:
        return m * power(m, n - 1)


def main():
    pass


if __name__ == "__main__":
    main()
