### Queue data structure

A queue is a fundamental data structure in computer science that follows the First-In, First-Out (FIFO) principle. This
means that the first element added to the queue will be the first one to be removed. Queues are used in various
applications such as scheduling processes, handling requests in web servers, and managing tasks in breadth-first search
algorithms.

#### Characteristics of a Queue

* FIFO Principle: The first element added is the first to be removed.
* Linear Structure: Elements are arranged in a linear sequence.
* Dynamic or Fixed Size: Queues can be implemented with a fixed size or can dynamically grow as needed.
* Two Ends: Operations are performed at two distinct ends—rear for enqueueing and front for dequeueing.

#### Core Operations

Queues support a limited set of operations that manipulate the elements. The primary operations are:

* Enqueue
* Dequeue
* Peek (or Front)
* isEmpty
* isFull (for fixed-size queues)
* Size

#### Python Implementation
```python
class Queue:
    def __init__(self, max_size=None):
        self.items = []
        self.max_size = max_size

    def enqueue(self, item):
        if self.max_size and self.size() >= self.max_size:
            raise OverflowError("Enqueue on full queue")
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Dequeue from empty queue")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Peek from empty queue")

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        if self.max_size:
            return len(self.items) >= self.max_size
        return False

    def size(self):
        return len(self.items)

```
