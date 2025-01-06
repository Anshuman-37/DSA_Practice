# Question 194: Implement a priority queue using a library function.
import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        if self.is_empty():
            return None
        return heapq.heappop(self.elements)[1]

pq = PriorityQueue()
pq.put('Task A', 3)
pq.put('Task B', 1)
pq.put('Task C', 2)

print("Processing tasks in order of priority:")
print(pq.get())
print(pq.get())
print(pq.get())