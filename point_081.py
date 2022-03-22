#!/usr/bin/env python3

class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def midpoint(self, other):
        x = (self.x + other.x) / 2
        y = (self.y + other.y) / 2
        p = Point(x, y)
        return p

    def __str__(self):
        return f"({self.x:.1f}, {self.y:.1f})"

def main():
    pass


if __name__ == "__main__":
    main()
