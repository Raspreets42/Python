class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class MergeTwoSorted():
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = node
        node.prev = cur

    def display(self):
        if self.head is None:
            print('List is empty')
            return
        cur = self.head
        print("head",end="")
        while cur:
            print(" <-->",cur.data,end="")
            cur = cur.next
        print(" <--> Null")


s1 = MergeTwoSorted()
s2 = MergeTwoSorted()
s1.insert(1)
s2.insert(2)
s2.insert(3)
s1.insert(4)
s1.insert(5)
s1.display()
s2.display()


def mergeTwoSortedList(s1, s2):
    l = MergeTwoSorted()
    l1 = s1.head
    l2 = s2.head
    while l1 and l2:
        if l1.data < l2.data:
            l.insert(l1.data)
            l1 = l1.next
        if l2.data < l1.data:
            l.insert(l2.data)
            l2 = l2.next
    while l1:
        l.insert(l1.data)
        l1 = l1.next
    while l2:
        l.insert(l2.data)
        l2 = l2.next
    l.display()

mergeTwoSortedList(s1,s2)