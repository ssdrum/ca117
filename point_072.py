#!/usr/bin/env python3

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, p):
        return ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** (1 / 2)

    def __str__(self):
        return f"({self.x:.1f}, {self.y:.1f})"


def main():
    pass


if __name__ == "__main__":
    main()
