#!/usr/bin/env python

# Two circles overlap if the sum of their radii is bigger than than the distance
# between their origins
def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
    horiz_d = x1 - x2
    vert_d = y1 - y2
    dist = (horiz_d * horiz_d + vert_d * vert_d) ** (1 / 2)

    return True if r1 + r2 > dist else False


if __name__ == '__main__':
   main()
