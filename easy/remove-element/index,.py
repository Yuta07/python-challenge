from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        
        for i in range(len(nums)):
            for j in nums:
                if j == val:
                    nums.remove(j)
                    
        return len(nums)