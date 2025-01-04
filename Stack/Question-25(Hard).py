# Question 175: Implement a stack using a queue.
from collections import deque


class Stack:
    def __init__(self):
        self.q = deque()

    def push(self, x):
        size = len(self.q)
        self.q.append(x)
        for _ in range(size):
            self.q.append(self.q.popleft())

    def pop(self):
        if not self.q:
            return None
        return self.q.popleft()

    def top(self):
        if not self.q:
            return None
        return self.q[0]

    def empty(self):
        return not self.q

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.top())
print(stack.pop())
print(stack.pop())  
print(stack.empty())
print(stack.pop())