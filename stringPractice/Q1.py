# Write a Python function to count the number of vowels in a string

str1 = "Hello World!"
vowels = "aeiouAEIOU"
count=0
for letter in str1:
    if letter in vowels:
        count=count+1

print(f"There are {count} vowels in this string")