#!/usr/bin/env python3

import sys

def isQnou(w):
    w = w.lower().replace("qu", "")
    rturn True if "q" in w else False


output = [w.strip() for w in sys.stdin if isQnou(w)]
print(f"Words with q but no u: {output}")
