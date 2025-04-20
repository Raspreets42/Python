# Reverse a string without using slicing ([::-1])

str1 = "Hello World!"
reversedStr = ''
for letter in str1:
    reversedStr = letter + reversedStr
print(reversedStr)