# Question 6: Get the min or max element of a heap without removing it.
def get_min_element(min_heap):
    if not min_heap:
        return None
    return min_heap[0]

def get_max_element(max_heap):
    if not max_heap:
        return None
    return max_heap[0]

min_heap = [2, 5, 8, 9, 11]
min_val = get_min_element(min_heap)
print(f"Minimum element of the min-heap: {min_val}")

empty_min_heap = []
min_val_empty = get_min_element(empty_min_heap)
print(f"Minimum element of the empty min-heap: {min_val_empty}")

max_heap = [15, 11, 10, 9, 8, 5, 2]
max_val = get_max_element(max_heap)
print(f"Maximum element of the max-heap: {max_val}")

empty_max_heap = []
max_val_empty = get_max_element(empty_max_heap)
print(f"Maximum element of the empty max-heap: {max_val_empty}")