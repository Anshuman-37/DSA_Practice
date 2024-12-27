# Question 19: Sort an almost sorted (k-sorted) array.

import heapq

def sort_k_sorted_array(arr, k):
    n = len(arr)
    heap = arr[:k + 1]
    heapq.heapify(heap)

    output_index = 0

    for i in range(k + 1, n):
        arr[output_index] = heapq.heappop(heap)
        heapq.heappush(heap, arr[i])
        output_index += 1

    while heap:
        arr[output_index] = heapq.heappop(heap)
        output_index += 1

    return arr

arr = [6, 5, 3, 2, 8, 10, 9]
k = 3
sorted_arr = sort_k_sorted_array(arr, k)
print("Sorted array:", sorted_arr)