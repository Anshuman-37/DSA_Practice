# Question 178: Design a max-stack data structure with push, pop, top, peekMax, and popMax operations.
class MaxStack:
    def __init__(self):
        self.main_stack = []
        self.max_stack = []

    def push(self, x):
        self.main_stack.append(x)
        if not self.max_stack or x >= self.max_stack[-1]:
            self.max_stack.append(x)

    def pop(self):
        if self.main_stack:
            if self.main_stack[-1] == self.max_stack[-1]:
                self.max_stack.pop()
            return self.main_stack.pop()

    def top(self):
        if self.main_stack:
            return self.main_stack[-1]

    def peekMax(self):
        if self.max_stack:
            return self.max_stack[-1]

    def popMax(self):
        if self.max_stack:
            max_val = self.max_stack[-1]
            temp_stack = []
            while self.main_stack[-1] != max_val:
                temp_stack.append(self.main_stack.pop())
            self.main_stack.pop()
            self.max_stack.pop()
            while temp_stack:
                self.push(temp_stack.pop())
            return max_val

max_stack = MaxStack()
max_stack.push(5)
max_stack.push(1)
max_stack.push(5)

print(max_stack.top())
print(max_stack.popMax())
print(max_stack.top())
print(max_stack.peekMax())
print(max_stack.pop())
print(max_stack.top())