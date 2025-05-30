from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest_seq = 0
        left, right = 0, 0
        num_zeros = 0

        while right < len(nums):
            if nums[right] == 0:
                num_zeros += 1
            while num_zeros == 2:
                if nums[left] == 0:
                    num_zeros -= 1
                left += 1
            longest_seq = max(longest_seq, right - left + 1)
            right += 1

        return longest_seq