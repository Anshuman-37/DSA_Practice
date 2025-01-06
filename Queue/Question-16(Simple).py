# Question 196: Implement a queue using two stacks.
class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x: int) -> None:
        self.stack1.append(x)

    def dequeue(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if self.stack2:
            return self.stack2.pop()
        else:
            return -1

    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if self.stack2:
            return self.stack2[-1]
        else:
            return -1

    def empty(self) -> bool:
        """
        Returns true if the queue is empty, false otherwise.
        """
        return not self.stack1 and not self.stack2

queue = MyQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())
queue.enqueue(4)
print(queue.dequeue())
print(queue.peek())
print(queue.empty())
print(queue.dequeue())
print(queue.dequeue())
print(queue.empty())
print(queue.dequeue())