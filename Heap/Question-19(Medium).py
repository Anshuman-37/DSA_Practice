# Question 19: Merge k sorted arrays using a min-heap.
import heapq

def merge_k_sorted_arrays(arrays):
    min_heap = []
    merged_array = []

    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(min_heap, (arr[0], i, 0))

    while min_heap:
        value, array_index, element_index = heapq.heappop(min_heap)
        merged_array.append(value)

        if element_index + 1 < len(arrays[array_index]):
            next_element = arrays[array_index][element_index + 1]
            heapq.heappush(min_heap, (next_element, array_index, element_index + 1))

    return merged_array

arrays = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged = merge_k_sorted_arrays(arrays)
print(f"Merged sorted array: {merged}")