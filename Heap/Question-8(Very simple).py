# Question 8: Find the k smallest element in a heap
import heapq

def find_kth_smallest_alternative(arr, k):
  if k <= 0 or k > len(arr):
    raise ValueError("Invalid value of k")

  min_heap = list(arr)
  heapq.heapify(min_heap)

  for _ in range(k - 1):
    heapq.heappop(min_heap)

  return heapq.heappop(min_heap)

arr = [7, 10, 4, 3, 20, 15]
k = 3
kth_smallest = find_kth_smallest_alternative(arr, k)
print(f"The {k}th smallest element is:", kth_smallest)

arr = [3, 2, 1, 5, 6, 4]
k = 2
kth_smallest = find_kth_smallest_alternative(arr, k)
print(f"The {k}th smallest element is:", kth_smallest)