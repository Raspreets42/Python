class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        print("Stack is empty")

    def topPeek(self):
        if not self.isEmpty():
            return self.stack[-1]
        print("Stack is empty")

    def display(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        for i, data in enumerate(self.stack):
            print(data, end=' ' if (i == len(self.stack) - 1) else ' --> ')
        print()


# Reverse a string using stack
def reverseString(strr):
    s = Stack()
    for ch in strr:
        s.push(ch)
    strr = ''
    while not s.isEmpty():
        strr = strr + s.topPeek()
        s.pop()

    return strr


print(reverseString("abcd"))


# Check for balanced parentheses
def check(st):
    stack = Stack()
    mapping = {")": "(", "}": "{", "]": "["}
    for s in st:
        if s in mapping.values():
            stack.push(s)
        elif s in mapping.keys():
            if stack.isEmpty() or mapping[s] != stack.pop():
                return False
    return stack.isEmpty()


s = "[{}]"
print(check(s))


# Evaluate postfix expression
def evaluate(st):
    stack = Stack()
    op = {'+', '-', '*', '/'}
    for s in st:
        if s not in op and s.isdigit():
            stack.push(s)
        elif s in op:
            first = stack.pop()
            second = stack.pop()
            if s == '+':
                stack.push(int(second) + int(first))
            if s == '-':
                stack.push(int(second) - int(first))
            if s == '*':
                stack.push(int(second) * int(first))
            if s == '/':
                stack.push(int(second) / int(first))

    result = stack.pop()
    if stack.isEmpty():
        return result
    else:
        return 0


s = "15 7 1 1 + - / 3 * 2 1 1 + + -"
splited = s.split()
print(evaluate(splited))
