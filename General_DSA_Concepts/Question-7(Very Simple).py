#  Implement a Stack using an array.
stack = []

stack.append('1')
stack.append('2')
stack.append('3')
stack.append('4')
# How stack now looks visually 4(top of stack) <- 3 <- 2 <- 1(bottom of stack)

print("Stack top is ",stack[-1])

stack.pop()
print("New stack top is ", stack[-1])


# Implement stack using class
class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if self.size == 0:
            print("Stack is empty")
            return
        self.items.pop()

    def peek_top(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size == 0


Stack = Stack()

Stack.push(1)
Stack.push(2)
Stack.push(3)
Stack.push(4)

print("Stack top is ",Stack.peek_top())
print("Stack size is ", Stack.size())

print("Popping element ", Stack.peek_top())
Stack.pop()
print("Popping element ", Stack.peek_top())
Stack.pop()
print("Popping element ", Stack.peek_top())
Stack.pop()

print("Stack size after pop is ", Stack.size())
print("Stack top after pop is ", Stack.peek_top())
