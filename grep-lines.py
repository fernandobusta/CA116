#!/usr/bin/env python3

import sys

word = sys.argv[1]
lines = []

#input the values
s = input()
while s != 'end':
    lines.append(s)
    s = input()

#identifying the word
#elements of the list
i = 0
while i < len(lines):
    actual = lines[i]
    j = 0
    while j < len(actual) and actual[j] != word[0]:
        j += 1
    if j < len(actual):
        k = 1
        while k < len(word) and actual[j + k] == word[k]:
            k += 1
        if k >= len(word):
            print(actual)

    i += 1
