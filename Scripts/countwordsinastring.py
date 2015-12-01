# countwordsinastring.py
# 'Counts the number of individual words in a string. For added complexity read these string in from a text file and generate a summary.'
# Martyr2's Mega Project List
# 01.12.2015 19:25

import re

print('Please make sure that the textfile you want to check is in the same folder as this script.')
print('Please enter the name of the textfile you want to check without extension:')
fileName = input()
file = open(fileName + '.txt')
file = file.read()
count = len(re.findall(r'\w+', file))
print('Your file has ' + str(count) + ' words.')