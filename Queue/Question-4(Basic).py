# Question 184: Check if a queue is empty.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return item

    def peek(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.front.data

    def is_empty(self):
        return self.front is None

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())
print(queue.peek())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

