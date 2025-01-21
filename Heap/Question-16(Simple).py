# Question 16: Find the smallest range containing elements from k lists using a min-heap.
import heapq

def smallest_range_from_k_lists(lists):
    min_heap = []
    max_range_value = -float('inf')
    k = len(lists)
    pointers = [0] * k

    for i in range(k):
        if lists[i]:
            heapq.heappush(min_heap, (lists[i][0], i))
            max_range_value = max(max_range_value, lists[i][0])

    smallest_range = [-float('inf'), float('inf')]

    while len(min_heap) == k:
        min_val, list_index = heapq.heappop(min_heap)

        current_range = max_range_value - min_val
        if current_range < smallest_range[1] - smallest_range[0]:
            smallest_range = [min_val, max_range_value]

        pointers[list_index] += 1
        if pointers[list_index] < len(lists[list_index]):
            next_val = lists[list_index][pointers[list_index]]
            max_range_value = max(max_range_value, next_val)
            heapq.heappush(min_heap, (next_val, list_index))
        else:
            break

    return smallest_range

lists = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
smallest_range = smallest_range_from_k_lists(lists)
print(f"Smallest range: {smallest_range}")