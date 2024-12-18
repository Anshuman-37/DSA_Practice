# Question 25:Maximum of all subarrays of size k (Sliding Window Maximum).

from collections import deque

def max_sliding_window_average(nums, k):
    n = len(nums)
    result = []
    dq = deque()  # Store indices of useful elements in the window

    for i in range(n):
        # Remove elements out of the current window
        if dq and dq[0] <= i - k:
            dq.popleft()

        # Remove elements smaller than the current element (from the right)
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)  # Add the current element's index
        # Add the  maximum (leftmost element in dq) to the result
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result

nums = [1,3,-1,-3,5,3,6,7]
k = 3

print(max_sliding_window_average(nums, k))
