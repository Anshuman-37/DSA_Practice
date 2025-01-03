# Question 14: Implement a stack that supports getMin() in O(1) without using extra space.
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_element = float('inf')

    def push(self, value):
        if not self.stack:
            self.stack.append(value)
            self.min_element = value
        elif value <= self.min_element:
            self.stack.append(2 * value - self.min_element)
            self.min_element = value
        else:
            self.stack.append(value)

    def pop(self):
        if not self.stack:
            return None
        top = self.stack.pop()
        if top <= self.min_element:
            ret = self.min_element
            self.min_element = 2 * self.min_element - top
            return ret
        else:
            return top

    def get_min(self):
        return self.min_element if self.stack else None

stack = MinStack()
stack.push(3)
stack.push(5)
stack.push(2)
stack.push(1)

print(stack.get_min())  # Output: 1
stack.pop()
print(stack.get_min())  # Output: 2