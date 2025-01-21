# Question 20: Find top k frequent elements in an array using a max-heap.
import heapq
from collections import Counter

def top_k_frequent_elements(nums, k):
    frequency_map = Counter(nums)
    max_heap = []

    for element, frequency in frequency_map.items():
        heapq.heappush(max_heap, (-frequency, element))

    top_k_elements = [heapq.heappop(max_heap)[1] for _ in range(k)]
    return top_k_elements

nums = [1, 1, 1, 2, 2, 3]
k = 2
top_k = top_k_frequent_elements(nums, k)
print(f"Top {k} frequent elements: {top_k}")