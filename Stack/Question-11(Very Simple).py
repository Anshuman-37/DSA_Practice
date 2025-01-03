# Question 11: Find the minimum element in a stack in O(1) time using an auxiliary stack
class MinStack:
    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, value):
        self.main_stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if not self.main_stack:
            return None
        popped_value = self.main_stack.pop()
        if popped_value == self.min_stack[-1]:
            self.min_stack.pop()
        return popped_value

    def top(self):
        if not self.main_stack:
            return None
        return self.main_stack[-1]

    def getMin(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]

stack = MinStack()
stack.push(3)
stack.push(5)
stack.push(2)
stack.push(1)

print(f"Minimum element: {stack.getMin()}")

stack.pop()
print(f"Minimum element after pop: {stack.getMin()}")

stack.pop()
print(f"Minimum element after pop: {stack.getMin()}")