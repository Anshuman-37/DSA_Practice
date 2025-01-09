# Question 3: Insert an element into a min-heap.
import math
def insert_into_min_heap(heap, value):
    heap.append(value)
    current_index = len(heap) - 1

    while current_index > 0:
        parent_index = math.floor((current_index - 1) / 2)
        if heap[current_index] < heap[parent_index]:
            heap[current_index], heap[parent_index] = heap[parent_index], heap[current_index]
            current_index = parent_index
        else:
            break

min_heap = [2, 5, 8, 9, 11]
value_to_insert = 4
print(f"Original min-heap: {min_heap}")

insert_into_min_heap(min_heap, value_to_insert)
print(f"Min-heap after inserting {value_to_insert}: {min_heap}")

min_heap2 = [10, 20, 30, 40, 50]
value_to_insert2 = 5
print(f"\nOriginal min-heap: {min_heap2}")

insert_into_min_heap(min_heap2, value_to_insert2)
print(f"Min-heap after inserting {value_to_insert2}: {min_heap2}")

min_heap3 = []
value_to_insert3 = 7
print(f"\nOriginal min-heap: {min_heap3}")
insert_into_min_heap(min_heap3, value_to_insert3)
print(f"Min-heap after inserting {value_to_insert3}: {min_heap3}")

value_to_insert4 = 3
insert_into_min_heap(min_heap3, value_to_insert4)
print(f"Min-heap after inserting {value_to_insert4}: {min_heap3}")