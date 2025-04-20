# Given a string, write a program to capitalize the first letter of each word

s = "raspreet Singh pasrija"

def CapitalizeFirstLetter(s):
    capstr = ''
    word = s.split()
    for w in word:
        capstr += w.capitalize() + ' '
    return capstr

print(CapitalizeFirstLetter(s))

def CapitalizeFirstLetterUsingTitle(s):
    return s.title()

print(CapitalizeFirstLetterUsingTitle(s))