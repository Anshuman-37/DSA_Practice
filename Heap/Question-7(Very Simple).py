# Question 7: Convert a min-heap to a max-heap.
def convert_min_heap_to_max_heap(min_heap):
    n = len(min_heap)
    for i in range(n // 2 - 1, -1, -1):
        _max_heapify(min_heap, i, n)


def _max_heapify(arr, index, heap_size):
    left = 2 * index + 1
    right = 2 * index + 2
    largest = index

    if left < heap_size and arr[left] > arr[largest]:
        largest = left
    if right < heap_size and arr[right] > arr[largest]:
        largest = right
    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        _max_heapify(arr, largest, heap_size)


min_heap = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
print("Original min-heap:", min_heap)

convert_min_heap_to_max_heap(min_heap)
print("Converted max-heap:", min_heap)
