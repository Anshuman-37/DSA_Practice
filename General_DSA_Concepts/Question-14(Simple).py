# Question 14: Implement a Stack using a Linked List.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def peek_top(self):
        if self.top is None:
            print("The stack is empty")
            return
        print(f"The value at the top of the stack is {self.top.data}")

    def push(self, x):
        if self.top is None:
            self.top = Node(x)
            self.top.next = None

        new_top = Node(x)
        new_top.next = self.top
        self.top = new_top

    def pop(self):
        if self.top is None:
            print("The stack is Empty")
            return
        print(f"Popping element {self.top.data}")
        self.top = self.top.next

    def traverse_stack(self):
        temp = self.top
        while temp.next:
            print(temp.data)
            temp = temp.next

Stack = Stack()

Stack.push(1), Stack.push(2), Stack.push(3), Stack.push(4)

print("This is how the current stack looks like")
Stack.traverse_stack()

Stack.pop()
Stack.pop()

print("This is how the current stack looks like")
Stack.traverse_stack()