# Implement a function that removes all special characters from a string

s = "Ras#123 &22"

def removeSpecialChars(s):
    result = ''
    for c in s:
        if c.isalnum() or c.isspace():
            result += c
        else:
            continue
    return result

print(removeSpecialChars(s))