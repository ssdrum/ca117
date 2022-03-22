#!/usr/bin/env python3

class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def midpoint(self, other):
        x = (self.x + other.x) / 2
        y = (self.y + other.y) / 2
        return Point(x, y)

    def __str__(self):
        return f"({self.x:.1f}, {self.y:.1f})"


class Circle(object):

    def __init__(self, centre=None, radius=1):
        self.centre = Point(0, 0) if centre is None else centre
        self.radius = radius

    def __str__(self):
        output = []
        output.append(f"Centre: ({self.centre.x:.1f}, {self.centre.y:.1f})")
        output.append(f"Radius: {self.radius}")
        return "\n".join(output)


def main():
    pass


if __name__ == "__main__":
    main()
