# Write a function that removes all occurrences of a given element from a list

list1=[1,2,4,4,8,6,9,8,9,1]
ele = 4

print([x for x in list1 if x != ele])

# while ele in list1:
#     list1.remove(ele)
#
# print(list1)
