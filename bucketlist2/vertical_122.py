#!/usr/bin/env python3

import sys

lines = [line.strip() for line in sys.stdin]
vert_lines = []

# find vertical lines and store in list
def verticalise():
    for i in range(len(lines[0])):
        vert_line = ""
        for line in lines:
            vert_line += line[i]
        vert_lines.append(vert_line)


# sorts vertical lines alphabetically
def sort_lines():
    vert_lines.sort(key=str.lower)


# re-horizontalise sorted vertical lines
def horizontalise():
    output = []

    for i in range(len(vert_lines[0])):
        horiz_line = ""
        for line in vert_lines:
            horiz_line += line[i]
        output.append(horiz_line)

    return "\n".join(output)


def main():
    verticalise()
    sort_lines()
    print(horizontalise())


if __name__ == "__main__":
    main()
