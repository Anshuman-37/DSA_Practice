# Question 180: Use a monotonic stack to find the maximum sum subarray efficiently.
def max_sum_subarray(nums):
    max_sum = 0
    stack = []

    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] > num:
            j = stack.pop()
            k = stack[-1] if stack else -1
            max_sum = max(max_sum, nums[j] * (i - k - 1))
        stack.append(i)

    while stack:
        j = stack.pop()
        k = stack[-1] if stack else -1
        max_sum = max(max_sum, nums[j] * (len(nums) - k - 1))

    return max_sum

nums = [2, 1, 5, 6, 2, 3]
result = max_sum_subarray(nums)
print(result)