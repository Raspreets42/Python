class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def getLength(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length

    def isEmpty(self):
        return self.getLength() == 0

    def displayNodes(self):
        if self.isEmpty():
            print("Empty List")
            return
        current = self.head
        print("head",end="")
        while current:
            print(" <-->",current.data,end="")
            current = current.next
        print(" <--> Null")


    def insertAtBeginning(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode

    def insertAtEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = newNode
        newNode.prev = current

    def insertAtPosition(self, data, position):
        if position == 0:
            self.insertAtBeginning(data)
            return
        if position == self.getLength():
            self.insertAtEnd(data)
            return
        if position < 0 or position >= self.getLength():
            raise ValueError("Position out of range")
        newNode = Node(data)
        current = self.head
        while position-1 > 0:
            current = current.next
            position -= 1
        newNode.prev = current
        newNode.next = current.next
        current.next = newNode

    def deleteFirstNode(self):
        if self.isEmpty():
            print("Empty List")
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def deleteEndNode(self):
        if self.isEmpty():
            print("Empty List")
            return
        current = self.head
        while current.next:
            current = current.next
        if current.prev:
            current.prev.next = None
        else:
            self.head = None

    def deleteNodeAtPosition(self, position):
        if position == 0:
            self.deleteFirstNode()
        if position == self.getLength()-1:
            self.deleteEndNode()
        if position < 0 or position >= self.getLength():
            raise ValueError("Position out of range")

    def backwardTraversal(self):
        current = self.head
        while current.next:
            current = current.next
        print("Null",end="")
        while current:
            print(" <-->", current.data,end="")
            current = current.prev
        print(" <--> head")


dl = DoublyLinkedList()
# dl.displayNodes()
dl.insertAtBeginning(1)
dl.insertAtBeginning(2)
dl.insertAtBeginning(3)
# dl.displayNodes()
dl.insertAtEnd(4)
dl.insertAtEnd(5)
dl.displayNodes()
dl.backwardTraversal()

# dl.insertAtPosition(9, 5)
# dl.displayNodes()

# dl.deleteFirstNode()
# dl.displayNodes()

# dl.deleteEndNode()
# dl.displayNodes()

# dl.deleteNodeAtPosition(5)
# dl.displayNodes()


