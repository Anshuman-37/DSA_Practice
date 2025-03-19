from typing import List
from functools import cache


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # points = defaultdict(int)
        # max_number = 0
        # for num in nums:
        #     points[num] += num
        #     max_number = max(max_number, num)

        # @cache
        # def max_points(num):
        #     if num == 0:
        #         return 0
        #     if num == 1:
        #         return points[1]

        #     return max(max_points(num-1) , max_points(num-2) + points[num])
        # return max_points(max_number)
        if len(nums) == 1:
            return nums[0]

        maxNum = max(nums)
        n = maxNum + 1

        points = [0] * n
        for num in nums:
            points[num] += num

        dp = [0] * n
        dp[0] = points[0]
        dp[1] = points[1]

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + points[i])

        return dp[n - 1]
        
