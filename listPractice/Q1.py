# Write a Python program to find the second largest number in a list

l = [1,4]
def findSecondLargestNumber(l):
    if len(l) < 2:
        return None
    uniq = set(l)
    sortedL = sorted(uniq)
    return sortedL[len(uniq)-2]

print(findSecondLargestNumber(l))