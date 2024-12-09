# Question 21: Implement a Priority Queue using a binary heap.
class PriorityQueue:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def peek(self):
        if not self.is_empty():
            return self.heap[0]
        raise IndexError("Peek from an empty priority queue")

    def insert(self, item):
        self.heap.append(item)
        self._percolate_up(len(self.heap) - 1)

    def extract_min(self):
        if self.is_empty():
            raise IndexError("Extract from an empty priority queue")
        min_item = self.heap[0]
        last_item = self.heap.pop()
        if not self.is_empty():
            self.heap[0] = last_item
            self._percolate_down(0)
        return min_item

    def _percolate_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def _percolate_down(self, index):
        size = len(self.heap)
        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break

    def __str__(self):
        return str(self.heap)

if __name__ == "__main__":
    pq = PriorityQueue()

    pq.insert(5)
    pq.insert(3)
    pq.insert(17)
    pq.insert(10)
    pq.insert(84)
    pq.insert(19)
    pq.insert(6)
    pq.insert(22)
    pq.insert(9)

    print("Priority Queue:", pq)

    print("Peek:", pq.peek())

    while not pq.is_empty():
        print("Extracted Min:", pq.extract_min())
