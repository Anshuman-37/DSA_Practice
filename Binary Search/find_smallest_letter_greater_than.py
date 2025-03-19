from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1

        while left <= right:
            mid = (left + right) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
            ## Left will basically hold the correct letter which is closest to the target
        if left == len(letters):
            return letters[0]
        else:
            return letters[left]