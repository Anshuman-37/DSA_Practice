
class MaxHeap:
    def __init__(self, items=None):
        self._heap = []
        if items:
            self._heap = list(items)
            self._build_max_heap()

    def _parent_index(self, index):
        return (index - 1) // 2

    def _left_child_index(self, index):
        return 2 * index + 1

    def _right_child_index(self, index):
        return 2 * index + 2

    def _has_parent(self, index):
        return self._parent_index(index) >= 0

    def _has_left_child(self, index):
        return self._left_child_index(index) < len(self._heap)

    def _has_right_child(self, index):
        return self._right_child_index(index) < len(self._heap)

    def _parent(self, index):
        return self._heap[self._parent_index(index)]

    def _left_child(self, index):
        return self._heap[self._left_child_index(index)]

    def _right_child(self, index):
        return self._heap[self._right_child_index(index)]

    def _swap(self, index1, index2):
        self._heap[index1], self._heap[index2] = self._heap[index2], self._heap[index1]

    def _heapify_up(self):
        index = len(self._heap) - 1
        while self._has_parent(index) and self._parent(index) < self._heap[index]:
            self._swap(self._parent_index(index), index)
            index = self._parent_index(index)

    def _heapify_down(self):
        index = 0
        while self._has_left_child(index):
            larger_child_index = self._left_child_index(index)
            if self._has_right_child(index) and self._right_child(index) > self._left_child(index):
                larger_child_index = self._right_child_index(index)
            if self._heap[index] > self._heap[larger_child_index]:
                break
            else:
                self._swap(index, larger_child_index)
                index = larger_child_index

    def _build_max_heap(self):
        for i in range(len(self._heap) // 2 - 1, -1, -1):
            self._max_heapify(i)

    def _max_heapify(self, index):
        largest = index
        left = self._left_child_index(index)
        right = self._right_child_index(index)
        n = len(self._heap)

        if left < n and self._heap[left] > self._heap[largest]:
            largest = left

        if right < n and self._heap[right] > self._heap[largest]:
            largest = right

        if largest != index:
            self._swap(index, largest)
            self._max_heapify(largest)

    def push(self, item):
        self._heap.append(item)
        self._heapify_up()

    def peek(self):
        if self._heap:
            return self._heap[0]
        else:
            return None

    def pop(self):
        if not self._heap:
            return None
        if len(self._heap) == 1:
            return self._heap.pop()

        max_item = self._heap[0]
        self._heap[0] = self._heap.pop()
        self._heapify_down()
        return max_item

    def size(self):
        return len(self._heap)

    def is_empty(self):
        return len(self._heap) == 0

    def to_list(self):
        return list(self._heap)  

max_heap = MaxHeap()
max_heap.push(10)
max_heap.push(4)
max_heap.push(7)
max_heap.push(1)
max_heap.push(15)

print("Max-Heap:", max_heap.to_list())
print("Maximum element:", max_heap.peek())
print("Pop maximum:", max_heap.pop())
print("Max-Heap after pop:", max_heap.to_list())

max_heap_from_list = MaxHeap([3, 1, 4, 1, 5, 9, 2, 6])
print("\nMax-Heap from list:", max_heap_from_list.to_list())
print("Pop maximum:", max_heap_from_list.pop())
print("Max-Heap after pop:", max_heap_from_list.to_list())