#!/usr/bin/env python3

import sys

def binSearch(query, sortedList):
    low = 0
    high = len(sortedList) - 1

    while low <= high:
        mid = (low + high) // 2

        if sortedList[mid] < query:
            low = mid + 1

        elif sortedList[mid] > query:
            high = mid - 1

        else:
            return True

    return False


# save normal copy of all words and a lowercase version in two lists
lowerWords = []
words = []
for line in sys.stdin:
    lowerWords.append(line.strip().lower())
    words.append(line.strip())

# add word to list if its reversed and lowercase version is in lowerWords and has len > 4
print([w for w in words if len(w) > 4 and binSearch(w[::-1].lower(), lowerWords)])
