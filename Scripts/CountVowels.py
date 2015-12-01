# CountVowels.py
# 'Enter a string and the program counts the number of vowels in the text. For added complexity have it report a sum of each vowel found.'
# Martyr2's Mega Project List
# 01.12.2015 19:01

text = input()

def find_vowels(text):
    count = 0
    vowels = "aeiouAEIOU"
    a = "a"
    e = "e"
    i = "i"
    o = "o"
    u = "u"
    A = "A"
    E = "E"
    I = "I"
    O = "O"
    U = "U"

    vowela = 0
    vowele = 0
    voweli = 0
    vowelo = 0
    vowelu = 0
    vowelA = 0
    vowelE = 0
    vowelI = 0
    vowelO = 0
    vowelU = 0
    for letter in text:
        if letter in text:
            if letter in vowels:
                count += 1
        if letter in a:
            vowela += 1
        elif letter in e:
            vowele += 1
        elif letter in i:
            voweli += 1
        elif letter in o:
            vowelo += 1
        elif letter in u:
            vowelu += 1
        elif letter in A:
            vowelA += 1
        elif letter in E:
            vowelE += 1
        elif letter in I:
            vowelI += 1
        elif letter in O:
            vowelO += 1
        elif letter in U:
            vowelU += 1
    print (count)
    print ('Count of a:' + str(vowela))
    print ('Count of e:' + str(vowele))
    print ('Count of i:' + str(voweli))
    print ('Count of o:' + str(vowelo))
    print ('Count of u:' + str(vowelu))
    print ('Count of A:' + str(vowelA))
    print ('Count of E:' + str(vowelE))
    print ('Count of I:' + str(vowelI))
    print ('Count of O:' + str(vowelO))
    print ('Count of U:' + str(vowelU))

find_vowels(text)