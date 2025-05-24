class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)
        print(value, "enqueued to the queue")

    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue underflow")
        else:
            value = self.queue.pop(0)
            print(value, "dequeued from the queue")

    def peek(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Front element is", self.queue[0])

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Queue elements:", self.queue)

q = Queue()

q.enqueue(32)
q.enqueue(40)
q.enqueue(60)
q.enqueue(12)
q.enqueue(18)
q.enqueue(56)
q.enqueue(87)

q.display()

q.peek()
q.dequeue()
q.display()

if q.is_empty():
    print("Queue is empty")
else:
    print("Queue is not empty")
