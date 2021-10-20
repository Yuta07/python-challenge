class Solution:
    def romanToInt(self, s: str) -> int:
        roman_symbol = { "I": 1, "V": 5, "X":10, "L": 50, "C": 100, "D": 500, "M": 1000 }

        romanStack = []

        for i in range(len(s)):
            roman = s[i]
            romanStack.append(roman)

        sum = 0
        prev = romanStack.pop()
        sum += roman_symbol[prev]
        
        for _ in range(len(romanStack)):
            cur = romanStack.pop()

            if roman_symbol[cur] >= roman_symbol[prev]:
                sum = sum + roman_symbol[cur]
            else:
                sum = sum - roman_symbol[cur]
                
            prev = cur
        
        return sum