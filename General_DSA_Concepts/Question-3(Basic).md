### Stack Data Structure

A stack is a fundamental data structure in computer science that follows the Last-In, First-Out (LIFO) principle.
This means that the most recently added element is the first one to be removed. Stacks are used in various applications,
including function call management in programming languages, expression evaluation, and undo mechanisms in software
applications.

#### Characteristics of a Stack 
* LIFO Principle: The last element added to the stack is the first one to be removed.
* Linear Structure: Elements are arranged in a linear sequence.
* Dynamic Size: The size of the stack can grow or shrink dynamically as elements are added or removed.
* Restricted Access: Operations are performed only at one end, known as the top of the stack.

#### Core Operations
Stacks support a limited set of operations that manipulate the elements. The primary operations are:
* Push
* Pop
* Peek (or Top)
* isEmpty
* Size

#### Python Implementation
```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Pop from empty stack")
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Peek from empty stack")
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

```