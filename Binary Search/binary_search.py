from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left , right = 0, len(nums) - 1

        while left <= right:
            # Get the middle index and the middle value.
            mid = (left + right) // 2

            # Case 1, return the middle index.
            if nums[mid] == target:
                return mid
            # Case 2, discard the smaller half.
            elif nums[mid] < target:
                left = mid + 1
                # Case 3, discard the larger half.
            else:
                right = mid - 1

        # If we finish the search without finding target, return -1.
        return -1
