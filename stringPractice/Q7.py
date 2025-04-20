# Write a Python program to find the most frequent character in a string
from collections import Counter

str1="Raspreet"
def findMostFrequentWord(st):
    counts = Counter(st)
    return max(counts, key=counts.get)
print(findMostFrequentWord(str1))

def findMostFrequentWordUsinMostCommon(st):
    counts = Counter(st)
    return counts.most_common(1)
print(findMostFrequentWordUsinMostCommon(str1))
