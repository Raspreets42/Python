class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class FindMiddle():
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

    def findM(self):
        if self.head is None:
            print('List is empty')
            return None
        start = self.head
        end = self.head
        while end.next is not None:
            start =  start.next
            end = end.next.next
            if start == end:
                return start.data


s = FindMiddle()
s.insert(1)
s.insert(2)
s.insert(3)
s.insert(4)
s.insert(5)
s.display()
print(s.findM())
