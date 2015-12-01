# PigLatin.py
# 'Pig Latin is a game of alterations played on the English language game. To  create the Pig Latin form of an English word the inital consonant sound is transposed to the end of the word and an ay is affixed(Ex.: "banana" would yield anana-bay). Red Wikipedia for more information on rules.'
# Martyr2's Mega Project List
# 01.12.2015 18:57

Word = input()
firstLetter = Word[0]
followingLetters = Word[1:]

print(followingLetters + '-' + firstLetter + 'ay')