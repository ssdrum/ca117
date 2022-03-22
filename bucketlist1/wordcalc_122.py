#!/usr/bin/env python3

import sys

definitions = {}

def define(var_name, i):
    if var_name.islower() and var_name.isalpha() and len(var_name) <= 30:
        try:
            i = int(i)
            if -1000 <= i and i <= 1000:
                if i not in definitions.values():
                    definitions[var_name] = i
        except TypeError:
            pass


def calc(tokens):
    try:
        tot = definitions[tokens[0]]
        operators = ["+", "-", "="]

        for i, t in enumerate(tokens):
            if t in operators:
                if t == "+":
                    tot += definitions[tokens[i + 1]]
                elif t == "-":
                    tot -= definitions[tokens[i + 1]]
                elif t == "=":
                    if tot in definitions.values():
                        for k, v in definitions.items():
                            if definitions[k] == tot:
                                return f"{' '.join(tokens)} {k}"
                    else:
                        return f"{' '.join(tokens)} unknown"
                else:
                    pass
    except KeyError:
        return f"{' '.join(tokens)} unknown"
    except IndexError:
        pass


def clear():
    definitions = {}


def main():
    for l in sys.stdin:
        tokens = l.split()
        if tokens[0] == "def":
            define(tokens[1], tokens[2])
        elif tokens[0] == "clear":
            clear()
        elif tokens[0] == "calc":
            print(calc(tokens[1:]))
        else:
            pass


if __name__ == "__main__":
    main()
