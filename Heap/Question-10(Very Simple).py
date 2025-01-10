# Question 10: Merge k sorted lists using a min-heap.
import heapq
def merge_k_sorted_lists(lists):
  min_heap = []
  result = []

  for i, lst in enumerate(lists):
    if lst:
      heapq.heappush(min_heap, (lst[0], i, 0))

  while min_heap:
    value, list_index, element_index = heapq.heappop(min_heap)
    result.append(value)

    if element_index + 1 < len(lists[list_index]):
      next_element = lists[list_index][element_index + 1]
      heapq.heappush(min_heap, (next_element, list_index, element_index + 1))

  return result

lists = [
  [1, 4, 5],
  [1, 3, 4],
  [2, 6]
]
merged_list = merge_k_sorted_lists(lists)
print("Merged list:", merged_list)

lists = [
  [],
  [1, 5],
  [2, 3, 6]
]
merged_list = merge_k_sorted_lists(lists)
print("Merged list:", merged_list)