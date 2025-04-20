mixedList = [1,"Apple",3,"Banana",5,"Coconut",7]

for i in mixedList:
    print(i)

print("---------------------------------")
print("Apple" in mixedList)

print("---------------------------------")
mixedList.append("Grapes")
print(mixedList)

print("---------------------------------")
print(mixedList.index("Grapes"))

print("---------------------------------")
# print(mixedList.sort())
# print(mixedList.sort(reverse=True))
print(mixedList.reverse())
print("---------------------------------")
print(mixedList.count("Apple"))
print("---------------------------------")
