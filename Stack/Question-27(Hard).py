# Question 177: Sort a stack using a single additional stack.
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

def sort_stack(stack):
    aux_stack = Stack()
    while not stack.is_empty():
        temp = stack.pop()
        while not aux_stack.is_empty() and aux_stack.peek() > temp:
            stack.push(aux_stack.pop())
        aux_stack.push(temp)
    while not aux_stack.is_empty():
        stack.push(aux_stack.pop())

stack = Stack()
stack.push(3)
stack.push(1)
stack.push(4)
stack.push(2)

sort_stack(stack)

while not stack.is_empty():
    print(stack.pop())