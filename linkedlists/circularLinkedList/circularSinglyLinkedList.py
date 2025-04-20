class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Empty List",end='')
            return
        temp = self.head
        while temp.next is not None:
            print(temp.data,end=' --> ')
            if temp.next == self.head:
                print( " --> (Back To Head) --> ", end="")


    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def emptyMyList(self):
        self.head = None

    def insertAtLast(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            node.next = None
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node
        node.next = self.head


l1 = CircularSinglyLinkedList()
l1.insertAtLast(1)
l1.insertAtLast(2)
l1.insertAtLast(3)
l1.insertAtLast(4)
l1.display()
print("")


