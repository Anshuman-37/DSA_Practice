# Question 5: Get the size of a stack.
class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [None] * capacity
        self.top = -1

    def push(self, item):
        if self.is_full():
            print("Stack Overflow")
            return

        self.top += 1
        self.stack[self.top] = item

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None

        item = self.stack[self.top]
        self.top -= 1
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[self.top]

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def size(self):
        return len(self.stack)


stack = Stack(5)
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.size())