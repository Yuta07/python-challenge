from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if i == len(nums) - 1 and target < nums[i]:
                return 0
            
            if i == len(nums) - 1 and target > nums[i]:
                return len(nums)

            if nums[i] == target:
                return i
            elif nums[i] < target and target < nums[i + 1]:
                return i + 1

    """
    // another solution
    
    if target > nums[-1]:
		return len(nums)
	else:
		for i in range(len(nums)):
			if target <= nums[i]:
				return i 
    """