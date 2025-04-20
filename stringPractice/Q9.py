# Check if a string contains only digits

s="3.4"
def checkForOnlyDigitsStr(s):
    if not s.isdigit():
        print("Not a only digit string")
    else:
        print("Only digit string")

checkForOnlyDigitsStr(s)