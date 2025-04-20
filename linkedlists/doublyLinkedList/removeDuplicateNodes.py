class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class RemoveDuplicate():
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

    def removeDuplicateNodes(self):
        if self.head is None:
            return
        cur = self.head
        while cur and cur.next:
            if cur.data == cur.next.data:
                dupli = cur.next
                cur.next = dupli.next
                if dupli.next:
                    dupli.next.prev = cur
                    del dupli
            else:
                cur = cur.next

s = RemoveDuplicate()
s.insert(1)
s.insert(1)
s.insert(1)
s.insert(1)
s.insert(1)
s.insert(1)
s.insert(1)
s.insert(1)
s.insert(1)
s.insert(2)
s.insert(2)
s.insert(3)
s.insert(4)
s.insert(5)
s.insert(5)
s.insert(6)
s.display()
s.removeDuplicateNodes()
s.display()