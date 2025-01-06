# Question 195: Use a queue to implement a stack.
from collections import deque

class Stack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, value):
        self.q1.append(value)

    def pop(self):
        if not self.q1:
            return None

        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        result = self.q1.popleft()

        self.q1, self.q2 = self.q2, self.q1
        return result

    def is_empty(self):
        return not self.q1

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.pop())
print(stack.pop())
print(stack.pop())