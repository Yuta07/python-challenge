class Solution:
    def mySqrt(self, x: int) -> int:
        result = 0
        for i in range(0, x + 1, 1):
            expo = i * i
                        
            if x == expo:
                result = i
                
                break
            elif x < expo:
                result = i - 1
                
                break
                        
        return result