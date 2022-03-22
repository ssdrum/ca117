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


def matcher(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    tokens = Stack()

    for c in s:
        if c in pairs.values():  # add char to stack if is an opening bracket
            tokens.push(c)
        elif c in pairs:
            try:  # avoids indexerror if first char is a closing bracket
                if tokens.pop() != pairs[c]:  # check if popped bracket corresponds to correct closing bracket
                    return False
            except IndexError:
                return False

    return True if len(tokens) == 0 else False  # return false if there are brackets left in stack


def main():
    tests = [
        '()',
        '(())',
        '(({}))',
        '(())(){}{(([]))}',
        '(()',
        '(()){()]',
        ')(()){([()])}'
    ]

    for test in tests:
        print(matcher(test.strip()))


if __name__ == "__main__":
    main()
