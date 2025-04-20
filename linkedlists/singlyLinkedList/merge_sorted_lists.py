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


l1 = LinkedList()
l1.insert(10)
l1.insert(12)
l1.insert(14)
l1.insert(16)
l1.insert(17)
l1.insert(18)
l1.insert(20)
l1.insert(24)
l1.display()

print()

l2 = LinkedList()
l2.insert(5)
l2.insert(15)
l2.insert(16)
l2.insert(17)
l2.insert(19)
l2.insert(21)
l2.insert(23)
l2.insert(27)
l2.insert(29)
l2.insert(30)
l2.insert(33)
l2.insert(37)
l2.insert(38)
l2.display()

def merge(l1, l2):
    l = LinkedList()
    t1 = l1.head
    t2 = l2.head
    while t1.next and t2.next:
        print(t1.data, t2.data)
        if t1.data <= t2.data:
            l.insert(t1.data)
            t1 = t1.next
        if t2.data <= t1.data:
            l.insert(t2.data)
            t2 = t2.next
    while t1:
        l.insert(t1.data)
        t1 = t1.next
    while t2:
        l.insert(t2.data)
        t2 = t2.next

    return l

print()
l = merge(l1,l2)
l.display()

