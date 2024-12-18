# Question 29: Minimum swaps required to sort the array.
"""
Explanation:
    arrpos: We create a list of pairs arrpos where each pair contains an element from nums and its original index.
    Sort: We sort arrpos based on the element values. Now, the second element of each pair in arrpos indicates the index where that element should be in the sorted array.
    vis: A boolean array to track visited elements during cycle detection.
Cycle Detection:
    We iterate through arrpos.
    If an element is already visited or is already in its correct position, we skip it.
    Otherwise, we start traversing the cycle using the index information in arrpos.
    We mark each visited element in vis.
    cycle_size keeps track of the number of elements in the current cycle.
Swaps: For each cycle, we add cycle_size - 1 to the ans.
Time Complexity: O(n log n) due to sorting. Cycle detection takes O(n) in total.
Space Complexity: O(n) for arrpos and vis.
Edge Cases:
    Empty array: Returns 0.
    Already sorted array: Returns 0.
"""


def min_swaps_optimal(nums):
    n = len(nums)
    arrpos = []
    for i in range(n):
        arrpos.append([nums[i], i])

    arrpos.sort()
    vis = [False] * n
    ans = 0

    for i in range(n):
        if vis[i] or arrpos[i][1] == i:
            continue
        cycle_size = 0
        j = i
        while not vis[j]:
            vis[j] = True
            j = arrpos[j][1]
            cycle_size += 1
        if cycle_size > 0:
            ans += (cycle_size - 1)
    return ans


nums = [2, 8, 10, 35, 0, 5, 4]
print(min_swaps_optimal(nums))
