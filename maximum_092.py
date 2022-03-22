#!/usr/bin/env python3

def maximum(l):
    if len(l) == 1:
        return l[0]
    if l[0] > l[1]:
        l.append(l[0])
        return maximum(l[1:])
    else:
        return maximum(l[1:])


def main():
    pass


if __name__ == "__main__":
    main()
