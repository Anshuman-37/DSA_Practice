from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]] | None:
        n = len(nums)
        if not nums:
            return [[lower, upper]]

        missing_ranges = []
        ## Taking care of missing ranges between lower bound and nums[0]
        if lower < nums[0]:
            missing_ranges.append([lower, nums[0] - 1])

        # Check for missing numbers between successive elements of nums.
        for i in range(n-1):
            if nums[i+1] - nums[i] <= 1:
                continue
            missing_ranges.append([nums[i] + 1, nums[i+1] - 1])
        # Check for any missing numbers between the last elements of nums and the upper bound
        if upper > nums[n-1]:
            missing_ranges.append([nums[n-1] + 1, upper])

        return missing_ranges


