#!/usr/bin/env python3

import sys
import string

def main():
    lines = [line for line in sys.stdin]  # save lines in list
    uni_words = {}  # store encountered words
    output = []

    for line in lines:
        out_line = []
        for w in line.split():
            strip_w = ""  # store a stripped, lowercase version of word in uni_words
            for c in w:
                if c not in string.punctuation:
                    strip_w += c
            strip_w = strip_w.lower()
            if strip_w not in uni_words:
                out_line.append(w)
                uni_words[strip_w] = True
            else:
                out_line.append(".")
        output.append(" ".join(out_line))

    print("\n".join(output))


if __name__ == "__main__":
    main()
