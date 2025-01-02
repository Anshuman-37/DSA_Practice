# Question 3: Implement a stack using a linked list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        item = self.head.data
        self.head = self.head.next
        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.head.data

    def is_empty(self):
        return self.head is None


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.pop())
print(stack.peek())