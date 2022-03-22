#!/usr/bin/env python3

import sys

vowels = "aeiou"
shortest = ""
iaryCount = 0
mostEs = []
esCount = 0


for word in sys.stdin:
    eCount = 0
    wordCpy = word.strip()
    word = word.lower().strip()

    if all(c in word for c in vowels):
        if len(shortest) == 0:
            shortest = wordCpy
        elif len(word) < len(shortest):
            shortest = wordCpy

    if word[-4:] == "iary":
        iaryCount += 1

    if "e" in word:
        replaced = word.replace("e", "")
        numEs = len(word) - len(replaced)
        if numEs > esCount:
            esCount = numEs
            mostEs = [wordCpy]
        elif numEs == esCount:
            mostEs.append(wordCpy)


print(f"Shortest word containing all vowels: {shortest}")
print(f"Words ending in iary: {iaryCount}")
print(f"Words with most e's: {mostEs}")
