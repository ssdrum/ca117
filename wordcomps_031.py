#!/usr/bin/env python3

import sys

words = []
for line in sys.stdin:
    words.append(line.strip())

# Takes 3 input: a string, a letter, and a number. Return true if letter appears
# in s at least n times
def hasNLetter(s, letter, n):
    tot = 0
    for c in s:
        if c == letter:
            tot += 1
    if tot >= n:
        return True
    else:
        return False


def isAnagram(word1, word2):
    if len(word1) == len(word2) and word1 != word2:
        for c in word1:
            if c in word2:
                word2 = word2.replace(c, "", 1)
        if len(word2) > 0:
            return False
        else:
            return True
    else:
        return False


print(f"Words containing 17 letters: {[w for w in words if len(w) == 17]}")
print(f"Words containing 18+ letters: {[w for w in words if len(w) > 17]}")
print(f"Words with 4 a's: {[w for w in words if hasNLetter(w.lower(), 'a', 4)]}")
print(f"Words with 2+ q's: {[w for w in words if hasNLetter(w.lower(), 'q', 2)]}")
print(f"Words containing cie: {[w for w in words if 'cie' in w.lower()]}")
print(f"Anagrams of angle: {[w for w in words if isAnagram(w.lower(), 'angle')]}")
