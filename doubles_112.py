#!/usr/bin/env python3

import sys

vowels = {"a", "e", "i", "o", "u"}
words = {word.strip(): 0 for word in sys.stdin}

for word in words:
    doubles = 0
    i = 0
    while i < len(word) - 1:  # I would like to thatnk Darragh for this incredible tip that saved my life, marriage, and probably my career
        if word[i] in vowels and word[i] == word[i + 1]:
            doubles += 1
            i += 2
        else:
            i += 1
    words[word] = doubles

print(max(words.items(), key=lambda x: x[1])[0])
