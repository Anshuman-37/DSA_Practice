# Question 18: Check if a subarray with a given sum exists (subarray sum problem).

def find_subarray_with_sum(arr, target):
    prefix_sum_map = {}
    curr_sum = 0
    for i, num in enumerate(arr):
        curr_sum += num
        if curr_sum == target:
            return (0, i)
        if curr_sum - target in prefix_sum_map:
            return (prefix_sum_map[curr_sum - target] + 1, i)

        prefix_sum_map[curr_sum] = i
    return (-1, -1)


arr = [1, 4, 20, 3, 10, 5]
target = 33

start, end = find_subarray_with_sum(arr, target)
print(f"Subarray found from index {start} to {end}")
