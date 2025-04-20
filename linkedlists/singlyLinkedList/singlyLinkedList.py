class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("head",end='')
            return
        temp = self.head
        print("head", end='')
        while temp:
            print(' -> ',temp.data,end='')
            temp = temp.next

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def emptyMyList(self):
        self.head = None

    def getLength(self):
        size = 0
        temp = self.head
        while temp is not None:
            size += 1
            temp = temp.next
        return size

    def insertAtBeginning(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

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

    def insertAtIndex(self, data, index):
        if index < 0 or index > self.getLength():
            raise ValueError("Index out of range")
        newNode = Node(data)
        if index == 0:
            newNode.next = self.head
            self.head = newNode

        count = 0
        cur = self.head
        while cur is not None:
            if count == index-1-1:
                newNode.next = cur.next
                cur.next = newNode
            cur = cur.next
            count = count + 1

    def insertAtMiddle(self, data):
        mid = self.getLength() // 2
        self.insertAtIndex(data,mid)

    def deleteFirst(self):
        if self.head is None:
            return None
        self.head = self.head.next

    def deleteLast(self):
        if self.head is None:
            return None
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.getLength():
            print("Index out of range")
            raise ValueError("Index out of range")
        if index == 0:
            self.deleteFirst()
            return
        count = 0
        cur = self.head
        prev = None
        while cur and count < index:
            prev = cur
            cur = cur.next
            count += 1
        if cur is None:
            raise ValueError("Index out of range")
        prev.next = cur.next

    def deleteByValue(self, value):
        if self.head is None:
            return None
        if self.head.data == value:
            self.head = self.head.next
            return
        prev = None
        temp = self.head
        while temp and temp.data != value:
            prev = temp
            temp = temp.next

        if temp is None:
            raise ValueError("Value not in list")

        prev.next = temp.next

    def searchValue(self, value):
        if self.head is None:
            print("Value not present in the list")
            return
        temp = self.head
        count = 0
        while temp :
            if temp.data == value:
                print(f"{value} is present in the list at index {count}")
                return
            else:
                count = count + 1
                temp = temp.next

        print("Value not present in the list")
        return

    def findMiddle(self):
        s = self.getLength()
        mid = s // 2 if s % 2 != 0 else (s // 2) - 1
        count = 0
        cur = self.head
        while cur and count < mid:
            cur = cur.next
            count += 1
        print(f"Middle index: {mid}, and data : {cur.data}")

    def reverseList(self):
        prev = None
        cur = self.head
        while cur:
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode
        self.head = prev

    def rotateRightByK(self,k):
        if self.head is None:
            return

        length = self.getLength()
        temp = self.head
        k = k % length
        if k == 0:
            return
        jump = length - k - 1
        while (jump):
            temp = temp.next
            jump -= 1
        newNode = temp.next
        temp.next = None
        temp = newNode
        while temp.next is not None:
            temp = temp.next
        temp.next = self.head
        self.head = newNode

l1 = SinglyLinkedList()
l1.insertAtLast(1)
l1.insertAtLast(3)
# l1.display()
# print("")

l1.insertAtBeginning(4)
# l1.display()
# print("")

l1.insertAtLast(5)
# l1.display()
# print("")

l1.insertAtIndex(2,4)
# l1.display()
# print("")

l1.insertAtMiddle(9)
l1.display()
print("")

# l1.deleteFirst()
# l1.display()
# print("")
#
# l1.deleteLast()
# l1.display()
# print("")
#
# l1.deleteAtIndex(2)
# l1.display()
# print("")
#
# l1.deleteByValue(1)
# l1.display()
# print("")

# l1.searchValue(2)
# l1.findMiddle()

# l1.reverseList()
# l1.display()
# print("")

# l1.rotateRightByK(2)
# l1.display()
# print("")

# print(l1.isEmpty())
# l1.emptyMyList()
# print(l1.isEmpty())

