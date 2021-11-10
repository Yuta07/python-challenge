from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1.extend(nums2)
        nums1.sort()
        
        count = len(nums1) - (m + n)

        for i in reversed(nums1):
            if i == 0 and 0 < count:
                nums1.remove(i)
                count -= 1

            