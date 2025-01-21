#  Question 23: Implement a double-ended priority queue.
import heapq

class DoubleEndedPriorityQueue:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.elements = set()

    def insert(self, item):
        heapq.heappush(self.min_heap, item)
        heapq.heappush(self.max_heap, -item)
        self.elements.add(item)

    def get_min(self):
        while self.min_heap and self.min_heap[0] not in self.elements:
            heapq.heappop(self.min_heap)
        return self.min_heap[0] if self.min_heap else None

    def get_max(self):
        while self.max_heap and -self.max_heap[0] not in self.elements:
            heapq.heappop(self.max_heap)
        return -self.max_heap[0] if self.max_heap else None

    def delete_min(self):
        if self.min_heap:
            min_val = heapq.heappop(self.min_heap)
            if min_val in self.elements:
                self.elements.remove(min_val)

    def delete_max(self):
        if self.max_heap:
            max_val_neg = heapq.heappop(self.max_heap)
            max_val = -max_val_neg
            if max_val in self.elements:
                self.elements.remove(max_val)


depq = DoubleEndedPriorityQueue()
depq.insert(5)
depq.insert(2)
depq.insert(8)
depq.insert(1)

print(f"Min: {depq.get_min()}")
print(f"Max: {depq.get_max()}")

depq.delete_min()
print(f"Min after delete_min: {depq.get_min()}")

depq.delete_max()
print(f"Max after delete_max: {depq.get_max()}")