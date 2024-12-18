## Question - 26: Longest Increasing Subsequence.
"""
Explanation:
    Tails Array: We maintain an array tails where tails[i] is the smallest tail of all increasing subsequences of length i+1.
    Iteration: We iterate through the nums array.
    Extend LIS: If the current number num is greater than the last element in tails, it means we can extend the longest increasing subsequence by 1. We append num to tails.
    Binary Search: If num is not greater than the last element in tails, we use binary search to find the smallest tail in tails that is greater than or equal to num. We replace that tail with num. This is because using num gives us an increasing subsequence of the same length but with a smaller tail, which has the potential to be extended further later on.
Result: The length of tails is the length of the LIS.
Time Complexity: O(n log n). The outer loop iterates n times, and the binary search takes O(log n) time in each iteration.
Space Complexity: O(n) to store the tails array.
Edge Cases:
    Empty input array: Returns 0.
"""

def length_of_lis_optimal(nums):
    tails = []  # tails[i] is the smallest tail of all increasing subsequences of length i+1

    for num in nums:
        if not tails or num > tails[-1]:
            tails.append(num)  # Extend the longest increasing subsequence
        else:
            # Find the smallest tail that is greater than or equal to the current number
            l, r = 0, len(tails) - 1
            while l <= r:
                mid = (l + r) // 2
                if tails[mid] < num:
                    l = mid + 1
                else:
                    r = mid - 1
            tails[l] = num  # Replace that tail with the current number

    return len(tails), tails

nums = [10,9,2,5,3,18,0,1,7,35,48,41,22,101]
print(length_of_lis_optimal(nums))