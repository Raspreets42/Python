# Implement a function that checks if a string is a palindrome

st = "namana"

if st[0::] == st[::-1]:
    print(f"{st} is a palindrome")
else:
    print(f"{st} is not a palindrome")