from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''

        for d in digits:
            s += str(d)

        i = str(int(s) + 1)
        
        arr = []
        
        for n in i:
            arr.append(n)

        return arr