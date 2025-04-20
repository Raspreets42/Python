# Write a function to check if two strings are anagrams
from collections import Counter

str1 = "Hello"
str2 = "elloH"

if Counter(str1) == Counter(str2):
    print("Anagram")
else:
    print("Not An Anagram")