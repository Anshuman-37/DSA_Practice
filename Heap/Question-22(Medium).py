# Question 22: Implement increase-key and decrease-key operations in a heap.
class MinHeapWithKeyOperations:
    def __init__(self):
        self.heap = []
        self.position = {}

    def __len__(self):
        return len(self.heap)

    def _swap(self, i, j):
        self.position[self.heap[i]] = j
        self.position[self.heap[j]] = i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _heapify_up(self, k):
        parent = (k - 1) // 2
        while k > 0 and self.heap[k] < self.heap[parent]:
            self._swap(k, parent)
            k = parent
            parent = (k - 1) // 2

    def _heapify_down(self, k):
        left = 2 * k + 1
        right = 2 * k + 2
        smallest = k
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != k:
            self._swap(k, smallest)
            self._heapify_down(smallest)

    def push(self, item):
        self.heap.append(item)
        self.position[item] = len(self.heap) - 1
        self._heapify_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            item = self.heap.pop()
            del self.position[item]
            return item
        root = self.heap[0]
        last = self.heap.pop()
        del self.position[root]
        if self.heap:
            self.heap[0] = last
            self.position[last] = 0
            self._heapify_down(0)
        return root

    def decrease_key(self, old_value, new_value):
        if new_value >= old_value:
            raise ValueError("New value must be smaller than the old value for decrease_key")
        if old_value not in self.position:
            raise ValueError("Element not found in heap")

        index = self.position[old_value]
        self.heap[index] = new_value
        del self.position[old_value]
        self.position[new_value] = index
        self._heapify_up(index)

    def increase_key(self, old_value, new_value):
        if new_value <= old_value:
            raise ValueError("New value must be larger than the old value for increase_key")
        if old_value not in self.position:
            raise ValueError("Element not found in heap")

        index = self.position[old_value]
        self.heap[index] = new_value
        del self.position[old_value]
        self.position[new_value] = index
        self._heapify_down(index)

heap = MinHeapWithKeyOperations()
heap.push(10)
heap.push(5)
heap.push(20)

print(f"Heap: {heap.heap}")

heap.decrease_key(20, 2)
print(f"Heap after decrease_key(20, 2): {heap.heap}")

heap.increase_key(5, 15)
print(f"Heap after increase_key(5, 15): {heap.heap}")