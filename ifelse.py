def Calculate(n1,n2,op):
    if op == "+":
        print(f"The sum of {n1} and {n2} is {n1 + n2}")
    elif op == "-":
        print(f"The difference of {n1} and {n2} is {n1 - n2}")
    elif op == "*":
        print(f"The product of {n1} and {n2} is {n1 * n2}")
    elif op == "/":
        print(f"The division of {n1} is {n1 / n2}")
    elif op == "**":
        print(f"{n1} the power {n2} is {n1 ** n2}")
    elif op == "%":
        print(f"The quotient of {n1} is {n1 % n2}")

num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))

operator = input("Enter the operator to perform (+,-,*,/,**,%): ")

Calculate(num1,num2,operator)