# Implement a Queue using array

queue = []

queue.append('1')
queue.append('2')
queue.append('3')
queue.append('4')

print("Queue front is ", queue[0])
print("Queue rear is ", queue[-1])
print("Queue size is", len(queue))

print("De Queuing element ", queue.pop(0))
print("New Front is", queue[0])


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, x):
        self.items.append(x)

    def dequeue(self):
        if self.size == 0:
            print("Queue is empty")
            return
        self.items.pop(0)

    def isEmpty(self):
        return self.size == 0

    def head(self):
        return self.items[0]

    def tail(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

Queue = Queue()

Queue.enqueue(1)
Queue.enqueue(2)
Queue.enqueue(3)
Queue.enqueue(4)

print("Front of queue is ",Queue.head())
print("Tail of queue is ",Queue.tail())

print("De Queuing element ", Queue.head())
Queue.dequeue()
print("New front is ", Queue.head())

