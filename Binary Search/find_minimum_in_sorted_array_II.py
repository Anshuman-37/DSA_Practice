from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                # Minimum must be to the right of mid.
                left = mid + 1
            elif nums[mid] < nums[right]:
                # Minimum is at mid or to the left of mid.
                right = mid
            else:
                # When nums[mid] and nums[right] are equal,
                # we can't decide the side, so reduce the search space.
                right -= 1

        return nums[left]
