# Question 13: Implement a deque (double-ended queue)
from collections import deque

class Deque:
    def __init__(self):
        self.items = deque()

    def insert_front(self, value):
        self.items.appendleft(value)

    def insert_rear(self, value):
        self.items.append(value)

    def delete_front(self):
        if self.is_empty():
            return None
        return self.items.popleft()

    def delete_rear(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def get_front(self):
        if self.is_empty():
            return None
        return self.items[0]

    def get_rear(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

deque = Deque()
deque.insert_rear(10)
deque.insert_front(5)
deque.insert_rear(15)

print("Deque:", deque.items)
print("Front:", deque.get_front())
print("Rear:", deque.get_rear())

deque.delete_front()
deque.delete_rear()

print("Deque after deletions:", deque.items)