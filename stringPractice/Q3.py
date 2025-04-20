# Write a program to find the first non-repeating character in a string
from collections import Counter

st="aman"
nonRepeating=''

for letter in st:
    if letter not in nonRepeating:
        nonRepeating+=letter
    else:
        break

print(f"First Non-repeating sub-string: {nonRepeating}")

countsStr = Counter(st)
for s in st:
    if countsStr[s] == 1:
        print(s)
        break