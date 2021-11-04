from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = nums[0]

        for i in range(1, len(nums)):
            if curSum < 0:
                curSum = 0

            curSum += nums[i]
            maxSub = max(maxSub, curSum)

        return maxSub