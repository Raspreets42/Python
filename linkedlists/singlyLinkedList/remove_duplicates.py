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

    def remove_duplicates(self):
        if self.head is None:
            return

        uniq = set()
        cur = self.head
        uniq.add(cur.data)
        while cur.next:
            if cur.next.data in uniq:
                cur.next = cur.next.next
            else:
                uniq.add(cur.next.data)
                cur = cur.next




l1 = LinkedList()
l1.insert(45)
l1.insert(54)
l1.insert(45)
l1.insert(56)
l1.insert(76)
l1.insert(34)
l1.insert(68)
l1.insert(76)
l1.display()
print()
l1.remove_duplicates()
l1.display()


