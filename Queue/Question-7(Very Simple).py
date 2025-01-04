# Question 7: Implement a circular queue using an array.
class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.capacity

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("Queue is full")

        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        if self.is_empty():
            self.front = -1
            self.rear = -1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[self.front]

    def size(self):
        return self.count

cq = CircularQueue(5)

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
print("Queue:", cq.queue)
print("Front:", cq.peek())

cq.dequeue()
print("Queue after dequeue:", cq.queue)
print("Front:", cq.peek())

cq.enqueue(40)
cq.enqueue(50)
print("Queue:", cq.queue)  # Output: Queue: [None, 20, 30, 40, 50]

cq.enqueue(60) # This will use the wrapped around space
print("Queue:", cq.queue) # Output: Queue: [60, 20, 30, 40, 50]

cq.dequeue()
cq.dequeue()
cq.dequeue()
print("Queue after multiple dequeues:", cq.queue) # Output: Queue after multiple dequeues: [60, None, None, 40, 50]
print("Front:", cq.peek()) # Output: Front: 40

try:
    cq.enqueue(70)
    cq.enqueue(80)
    cq.enqueue(90) # This should raise an OverflowError
except OverflowError as e:
    print(e) # Output: Queue is full

print("Is empty:", cq.is_empty()) # Output: Is empty: False
print("Is full:", cq.is_full())   # Output: Is full: True
print("Size:", cq.size())       # Output: Size: 5