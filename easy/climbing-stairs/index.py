class Solution:
    def climbStairs(self, n: int) -> int:
        """
        1 -> 1
        2 -> 2
        3 -> 3
        4 -> 5
        5 -> 8
        6 -> 13
        7 -> 21
        8 -> 34
        9 -> 55
        10 -> 89
        """
        
        i = 1
        x = 0
        y = 1
        while i < n:
            x, y = y, x + y
            
            i += 1
        
        z = x + y
        
        return z