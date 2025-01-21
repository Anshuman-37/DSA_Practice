# Question 13: Implement a priority queue using a heap.
import heapq

class PriorityQueue:
    def __init__(self):
        self._heap = []
        self._index = 0

    def enqueue(self, item, priority):
        heapq.heappush(self._heap, (priority, self._index, item))
        self._index += 1

    def dequeue(self):
        if not self._heap:
            raise IndexError("dequeue from an empty priority queue")
        return heapq.heappop(self._heap)[2]

    def peek(self):
        if not self._heap:
            raise IndexError("peek from an empty priority queue")
        return self._heap[0][2]

    def is_empty(self):
        return not self._heap

    def size(self):
        return len(self._heap)

pq = PriorityQueue()
pq.enqueue("Task A", 3)
pq.enqueue("Task B", 1)
pq.enqueue("Task C", 4)
pq.enqueue("Task D", 2)

print("Priority Queue size:", pq.size())
print("Is the priority queue empty?", pq.is_empty())

print("Dequeue:", pq.dequeue())
print("Peek:", pq.peek())
print("Dequeue:", pq.dequeue())
print("Dequeue:", pq.dequeue())
print("Dequeue:", pq.dequeue())

print("Is the priority queue empty?", pq.is_empty())