# Question 205: Implement a priority queue from scratch using a binary heap.
class PriorityQueue:
    def __init__(self):
        self.heap = []

    def _parent(self, i):
        return (i - 1) // 2

    def _left_child(self, i):
        return 2 * i + 1

    def _right_child(self, i):
        return 2 * i + 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _heapify_up(self, index):
        while index > 0 and self.heap[index] < self.heap[self._parent(index)]:
            self._swap(index, self._parent(index))
            index = self._parent(index)

    def _heapify_down(self, index):
        min_index = index
        left = self._left_child(index)
        right = self._right_child(index)
        n = len(self.heap)

        if left < n and self.heap[left] < self.heap[min_index]:
            min_index = left

        if right < n and self.heap[right] < self.heap[min_index]:
            min_index = right

        if min_index != index:
            self._swap(index, min_index)
            self._heapify_down(min_index)

    def enqueue(self, item):
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def dequeue(self):
        if not self.heap:
            raise IndexError("dequeue from an empty priority queue")

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def peek(self):
        if not self.heap:
            raise IndexError("peek from an empty priority queue")
        return self.heap[0]

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)

if __name__ == "__main__":
    pq = PriorityQueue()
    pq.enqueue(3)
    pq.enqueue(1)
    pq.enqueue(4)
    pq.enqueue(1)
    pq.enqueue(5)
    pq.enqueue(9)
    pq.enqueue(2)
    pq.enqueue(6)

    print("Priority Queue:", pq.heap)

    print("Dequeue:", pq.dequeue())
    print("Dequeue:", pq.dequeue())
    print("Dequeue:", pq.dequeue())

    print("Peek:", pq.peek())

    print("Is Empty:", pq.is_empty())
    print("Size:", pq.size())

    while not pq.is_empty():
        print("Dequeue:", pq.dequeue())