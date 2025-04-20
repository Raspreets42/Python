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

    def reverse(self):
        stack = []




q = Queues()
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.display()