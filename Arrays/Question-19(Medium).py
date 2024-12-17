# Question 19: Smallest subarray with sum greater than a given value.

def smallest_subarray_sliding_window(arr, S):
    n = len(arr)
    min_length = n + 1
    current_sum = 0
    start = 0

    for end in range(n):
        current_sum += arr[end]

        while current_sum >= S:
            min_length = min(min_length, end - start + 1)
            current_sum -= arr[start]
            start += 1

    return min_length if min_length <= n else 0


A = [2, 1, 5, 2, 3, 2]
S = 7
print(smallest_subarray_sliding_window(A, S))
