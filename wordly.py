#!/usr/bin/env python
import string

""" Tile word game cheater """

sc_points = {'A': 1, 'B': 3, 'C': 3, 'E': 1, 'D': 2, 'G': 2, 'F': 4, 'I': 1, 'H': 4, 'K': 5, 'J': 8, 'M': 3, 'L': 1, 'O': 1, 'N': 1, 'Q': 10, 'P': 3, 'S': 1, 'R': 1, 'U': 1, 'T': 1, 'W': 4, 'V': 4, 'Y': 4, 'X': 8, 'Z': 10}

letters = raw_input('What letters do you have? ').upper()

words = open('TWL06.txt', 'r')
viables = [line.strip() for line in words if line[0] in letters]
words.close()

matches = {}
for entry in viables:
    temp = letters
    okay = True
    for letter in entry:
        if letter not in temp:
            okay = False
            break
        else:
            temp = temp.replace(letter, '', 1)
    if okay:
        val = 0
        for tile in entry:
            val+=sc_points[tile]
        matches[entry] = val

# playable = matches.items()
# print sorted(playable, key=lambda x: x[1], reverse=True)

for w in sorted(matches, key=matches.get, reverse=True):
    print w + ': ' + str(matches[w])