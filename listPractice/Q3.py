# Write a Python program to reverse a list without using the reverse() method

list1=[1,2,3,4,5,6,7,8,9,10]

def reverseListUsingReversed(l):
    return list(reversed(list1))
print("reverseListUsingReversed : " , reverseListUsingReversed(list1))


def reverseListUsingSlice(l):
    return l[::-1]
print("reverseListUsingSlice : " , reverseListUsingSlice(list1))

def reverseListUsingTwoPoints(l):
    lg = len(l)
    for i in range(lg//2):
        r = l[i]
        l[i] = l[lg-1-i]
        l[lg-1-i] = r
    return l
print("reverseListUsingTwoPoints : " , reverseListUsingTwoPoints(list1))