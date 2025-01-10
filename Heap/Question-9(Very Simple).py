# Question 9: Find the kth largest element in an array using a max-heap.
import heapq
def find_kth_largest_using_max_heap(arr, k):
  if k <= 0 or k > len(arr):
    raise ValueError("Invalid value of k")

  max_heap = [-x for x in arr[:k]]
  heapq.heapify(max_heap)

  for i in range(k, len(arr)):
    if arr[i] > -max_heap[0]:
      heapq.heapreplace(max_heap, -arr[i])

  return -max_heap[0]

arr = [3, 2, 1, 5, 6, 4]
k = 2
kth_largest = find_kth_largest_using_max_heap(arr, k)
print(f"The {k}th largest element is:", kth_largest)

arr = [7, 10, 4, 3, 20, 15]
k = 3
kth_largest = find_kth_largest_using_max_heap(arr, k)
print(f"The {k}th largest element is:", kth_largest)