class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_blank = s.split()
        last = s_blank[-1]
        
        return len(last)