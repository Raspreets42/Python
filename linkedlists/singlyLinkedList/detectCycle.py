class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        temp = self.head
        print("head", end="")
        while temp:
            print(" -> " , temp.data, end="")
            temp = temp.next

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(data)

    def createCycle(self, position):
        if position < 0:
            return None
        temp = self.head
        target = None
        index = 0
        while temp and temp.next:
            if index == position:
                target = temp.next
            temp = temp.next
            index += 1
        if temp and target:
            temp.next = target

    def detectCycle(self):
        slow = self.head  # Slow pointer moves one step
        fast = self.head  # Fast pointer moves two steps

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            print(f"slow: {slow.data}, fast: {fast.data}")  # Debugging output

            if slow == fast:  # If they meet, there's a cycle
                return True

        return False  # No cycle found


l1 = LinkedList()
l1.insert(10)
l1.insert(20)
l1.insert(30)
l1.insert(40)
l1.insert(50)
l1.display()
print()
print(l1.detectCycle())
l1.createCycle(2)
print(l1.detectCycle())


