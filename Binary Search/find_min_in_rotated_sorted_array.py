from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # If there is only one element then it is the smallest element
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1

        # Base Case this means that array is not rotated so basically return
        if nums[right] > nums[0]:
            return nums[0]

        #
        while right >= left:
            mid = left + (right - left) // 2
            # Check statements to return the found value
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            # Update boundaries
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1
