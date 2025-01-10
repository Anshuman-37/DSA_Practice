# Question 11: Sort an array using heap sort.
def heap_sort(arr):
  n = len(arr)

  for i in range(n // 2 - 1, -1, -1):
    _max_heapify(arr, i, n)
  for i in range(n - 1, 0, -1):
    arr[i], arr[0] = arr[0], arr[i]
    _max_heapify(arr, 0, i)

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

arr = [12, 11, 13, 5, 6, 7]
print("Original array:", arr)
heap_sort(arr)
print("Sorted array:", arr)

arr = [5, 1, 4, 2, 8]
print("Original array:", arr)
heap_sort(arr)
print("Sorted array:", arr)