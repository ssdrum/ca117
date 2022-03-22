#!/usr/bin/env python3

class Stack(object):

    def __init__(self):
        self.items = []

    def push(self, e):
        self.items.append(e)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)


def isDigit(n):  # improved isdigit function that handles floats
    try:
        float(n)
        return True
    except ValueError:
        return False


def sqrt(n):
    return n ** .5


def calculator(line):
    binops = {
        '+': float.__add__,
        '-': float.__sub__,
        '*': float.__mul__,
        '/': float.__truediv__
    }
    uniops = {
        'n': float.__neg__,
        'r': sqrt
    }
    nums = Stack()

    for token in line.split():
        if isDigit(token):
            nums.push(float(token))
        elif token in binops:
            first_n = nums.pop()
            second_n = nums.pop()
            nums.push(binops[token](second_n, first_n))
        elif token in uniops:
            n = nums.pop()
            nums.push(uniops[token](n))

    if len(nums) == 1:
        return nums.items[0]


def main():
    pass


if __name__ == "__main__":
    main()
