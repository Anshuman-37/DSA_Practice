# Question 22: Implement a sliding window maximum using a deque.
from collections import deque

def max_of_subarrays(nums, k):
    if not nums or k <= 0:
        return []

    n = len(nums)
    if k > n:
        return []

    dq = deque()
    result = []

    for i in range(n):
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result

# Example Usage:
nums1 = [1, 3, -1, -3, 5, 3, 6, 7]
k1 = 3
print(f"Maximums of subarrays of size {k1}: {max_of_subarrays(nums1, k1)}")

nums2 = [1, 2, 3, 1, 4, 5, 2, 3, 6]
k2 = 3
print(f"Maximums of subarrays of size {k2}: {max_of_subarrays(nums2, k2)}")

nums3 = [1]
k3 = 1
print(f"Maximums of subarrays of size {k3}: {max_of_subarrays(nums3, k3)}")

nums4 = [1, -1]
k4 = 1
print(f"Maximums of subarrays of size {k4}: {max_of_subarrays(nums4, k4)}")
