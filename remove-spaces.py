#!/usr/bin/env python3

s = input()

characters = len(s)
t = 0
final = ''
i = 0
while i < characters:
    letter_or_space = str(s[t])
    if (letter_or_space != ' '):
        final = final + s[t]
    else:
        final = final
    t += 1
    i += 1

print(final)
