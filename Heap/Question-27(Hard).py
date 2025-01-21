# Question 27: Find the maximum sum combination from two arrays using a max-heap.
import heapq

def max_sum_combinations(A, B, k):
    A.sort(reverse=True)
    B.sort(reverse=True)
    n = len(A)
    max_heap = [-(A[0] + B[0])]
    visited = {(0, 0)}
    result = []

    for _ in range(k):
        neg_sum = heapq.heappop(max_heap)
        result.append(-neg_sum)
        i, j = None, None
        current_sum = -neg_sum
        for row_idx in range(n):
            for col_idx in range(n):
                if A[row_idx] + B[col_idx] == current_sum and (row_idx, col_idx) in visited:
                    i, j = row_idx, col_idx
                    break
            if i is not None:
                break

        if i + 1 < n and (i + 1, j) not in visited:
            heapq.heappush(max_heap, -(A[i + 1] + B[j]))
            visited.add((i + 1, j))
        if j + 1 < n and (i, j + 1) not in visited:
            heapq.heappush(max_heap, -(A[i] + B[j + 1]))
            visited.add((i, j + 1))

    return result

A = [1, 4, 2, 3]
B = [5, 2, 6, 1]
k = 4
max_sums = max_sum_combinations(A, B, k)
print(f"Top {k} maximum sum combinations: {max_sums}")