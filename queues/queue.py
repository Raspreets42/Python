from collections import deque

cq = deque()

cq.append(10)   # enqueue
cq.append(20)
cq.popleft()    # dequeue
cq.appendleft(30)
print(cq)

class Queues:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if len(self.queue) == 0:
            return "Queue is empty"
        return self.queue.pop(0)

    def peek(self):
        return self.queue[0] if not self.isEmpty() else None

    def display(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        print("Front -->",end=" ")
        for i in self.queue:
            print(i,end=" --> ")
        print("Rear")


q = Queues()
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.display()
print("dequeue : ", q.dequeue())
q.display()
print("dequeue : ", q.dequeue())
q.display()
print("peek : ", q.peek())
q.display()

