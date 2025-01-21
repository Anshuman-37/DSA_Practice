# Question 24: Check if a given array represents a valid heap.
def is_valid_heap(arr, heap_type="min"):
    n = len(arr)
    for i in range((n // 2) - 1, -1, -1):
        left_child_index = 2 * i + 1
        right_child_index = 2 * i + 2

        if left_child_index < n:
            if heap_type == "min" and arr[i] > arr[left_child_index]:
                return False
            if heap_type == "max" and arr[i] < arr[left_child_index]:
                return False

        if right_child_index < n:
            if heap_type == "min" and arr[i] > arr[right_child_index]:
                return False
            if heap_type == "max" and arr[i] < arr[right_child_index]:
                return False

    return True


min_heap_array = [2, 3, 4, 5, 7, 6]
max_heap_array = [7, 6, 5, 4, 3, 2]
not_heap_array = [1, 5, 3, 2, 4]

print(f"Is min_heap_array a valid min-heap? {is_valid_heap(min_heap_array, 'min')}")
print(f"Is max_heap_array a valid max-heap? {is_valid_heap(max_heap_array, 'max')}")
print(f"Is not_heap_array a valid min-heap? {is_valid_heap(not_heap_array, 'min')}")
