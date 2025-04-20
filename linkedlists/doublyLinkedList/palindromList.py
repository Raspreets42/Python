class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class PalindromList():
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

    def checkForPalindrome(self):
        if self.head is None:
            return True
        start = self.head
        end = self.head
        while end.next is not None:
            end = end.next
        while start.next and end.prev:
            if start.data != end.data:
                return False
            else:
                start = start.next
                end = end.prev
        return True

d = PalindromList()
d.insert('a')
d.insert('n')
d.insert('a')
d.insert('m')
d.insert('a')
d.insert('n')
d.insert('a')
d.display()
print(d.checkForPalindrome())

