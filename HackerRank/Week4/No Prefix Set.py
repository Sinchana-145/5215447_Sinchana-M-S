import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#

def noPrefix(words):
    # Write your code here
    xyz = {}

    for word in words:
        node = xyz
        for i, ch in enumerate(word):
            if ch not in node:
                node[ch] = {}
            node = node[ch]
            if "_end_" in node:  
                print("BAD SET")
                print(word)
                return
        if node: 
            print("BAD SET")
            print(word)
            return
        node["_end_"] = True

    print("GOOD SET")

if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
