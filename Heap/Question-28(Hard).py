# Question 28: Find the kth smallest element in a row-wise and column-wise sorted matrix using a min-heap.
import heapq

def kth_smallest_in_sorted_matrix(matrix, k):
    rows = len(matrix)
    cols = len(matrix[0])
    min_heap = [(matrix[0][0], 0, 0)]
    visited = {(0, 0)}

    for _ in range(k - 1):
        value, r, c = heapq.heappop(min_heap)

        if c + 1 < cols and (r, c + 1) not in visited:
            heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1))
            visited.add((r, c + 1))

        if r + 1 < rows and (r + 1, c) not in visited:
            heapq.heappush(min_heap, (matrix[r + 1][c], r + 1, c))
            visited.add((r + 1, c))

    return min_heap[0][0]

matrix = [
    [1,  5,  9],
    [10, 11, 13],
    [12, 13, 15]
]
k = 8
kth_smallest = kth_smallest_in_sorted_matrix(matrix, k)
print(f"The {k}th smallest element is: {kth_smallest}")