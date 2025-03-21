# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        left, right = 0, 1

        # Step 1: Find out the boundaries
        while reader.get(right) < target and reader.get(right) != 2**31 - 1:
            left = right
            right *= 2

        # Step 2: Perform binary search within the found boundaries.
        while left <= right:
            mid = left + (right - left) // 2
            val = reader.get(mid)
            if val == target:
                return mid  # return the index
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1