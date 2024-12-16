# Question 13: Maximum Subarray Sum (Kadane’s Algorithm).

def max_subarray_sum(lst:list) -> int:
    n = len(lst)
    max_sum = lst[0]
    current_sum = lst[0]
    for i in range(1, n):
        current_sum = max(lst[i], current_sum + lst[i])
        max_sum = max(max_sum, current_sum)
    return max_sum


lst = [-2, -3, 4, -1, -2, 1, 5, -3]
print(f"Array: {lst}")
print(f"Maximum subarray sum: {max_subarray_sum(lst)}")
