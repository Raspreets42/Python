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


s = Stack()
s.display()
s.push(10)
s.display()
s.push(20)
s.display()
s.push(30)
s.display()
s.pop()
s.display()
s.pop()
s.display()
s.push(40)
s.display()
