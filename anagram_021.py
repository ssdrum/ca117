#!/usr/bin/env python3

import sys

def isAnagram(word1, word2):
    if len(word1) == len(word2):
        for c in word1:
            if c in word2:
                word2 = word2.replace(c, "", 1)
        if len(word2) > 0:
            return False
        else:
            return True
    else:
        return False

words = ["cat", "house",]

for w in words:
    words = line.split()
    print(isAnagram(words[0], words[1]))
