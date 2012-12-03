#!/usr/bin/env python
import string
import re

""" Tile word game cheater """

sc_points = {'A': 1, 'B': 3, 'C': 3, 'E': 1, 'D': 2, 'G': 2, 'F': 4, 'I': 1, 'H': 4, 'K': 5, 'J': 8, 'M': 3, 'L': 1, 'O': 1, 'N': 1, 'Q': 10, 'P': 3, 'S': 1, 'R': 1, 'U': 1, 'T': 1, 'W': 4, 'V': 4, 'Y': 4, 'X': 8, 'Z': 10, '*': 0}
wwf_points = {'*': 0, 'A': 1, 'C': 4, 'B': 4, 'E': 1, 'D': 2, 'G': 3, 'F': 4, 'I': 1, 'H': 3, 'K': 5, 'J': 10, 'M': 4, 'L': 2, 'O': 1, 'N': 2, 'Q': 10, 'P': 4, 'S': 1, 'R': 1, 'U': 2, 'T': 1, 'W': 4, 'V': 5, 'Y': 3, 'X': 8, 'Z': 10}
print 'What game are you playing?'
game = raw_input('Simple anagrams (i.e. Letterpress) (Press 1), Scrabble (Press 2), or Words with Friends (Press 3) ')
letters = raw_input('What letters do you have? ("*" = blank) ').upper()

if '*' in letters:
    letters.replace('*', '[A-Z]')

words = open('TWL06.txt', 'r')
viables = [line.strip() for line in words if line[0] in letters]
words.close()

matches = {}
for entry in viables:
    temp = letters
    okay = True
    blankTo = '*'
    for letter in entry:
        if letter not in temp and '*' not in temp:
            okay = False
            break
        elif letter in temp:
            temp = temp.replace(letter, '', 1)
        else:
            blankTo = letter
            temp = temp.replace('*', '', 1)
            
    if okay:
        val = 0
        for tile in entry:
            if int(game) == 2:
                val+=sc_points[tile]
            elif int(game) == 3:
                val+=wwf_points[tile]
            else:
                val  = 'there are no points in this pure endeavor, silly face';

        if int(game) == 2:
            val-=sc_points[blankTo]
        elif int(game) == 3:
            val-=wwf_points[blankTo]
        matches[entry] = val

if int(game) > 1:
    for w in sorted(matches, key=matches.get):
        print w + ': ' + str(matches[w])
else:
    for w in sorted(matches.keys(), key=len):
        print w