# Implement a function that removes all spaces from a string

st = "Raspreet Singh Pasrija"

def removeSpaceWithLoop(s):
    result = ''
    for i in s:
        if i != " ":
            result += i
        else:
            continue
    return result

def removeSpacesWithInBuitFunc(s):
    return s.replace(" ", "")

print( removeSpaceWithLoop(st) )
print( removeSpacesWithInBuitFunc(st) )