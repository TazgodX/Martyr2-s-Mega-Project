# CheckifPalindrome.py
# 'Checks if the string entered by the user is a palindrome. That is that it reads the same forwars as backwars like "racecar".'
# Martyr2's Mega Project List
# 01.12.2015 19:20

text = input()
text = text.lower()
textbackwards = text[::-1]

if text == textbackwards:
    print('The string you entered is Palindrome.')
else:
    print('The string you entered is NOT Palindrome.')