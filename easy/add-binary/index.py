class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

        # cnt = 0
        # m = 0
        # for i in range(len(a) - 1, -1, -1):
        #     x = 2**cnt * int(a[i])
        #     m += x
        #     cnt += 1
        
        # cnt = 0
        # n = 0
        # for j in range(len(b) - 1, -1, -1):
        #     x = 2**cnt * int(b[j])
        #     n += x
        #     cnt += 1
        
        # sum = m + n

        # arr = []

        # if sum == 0:
        #     arr =['0']
            
        # while sum > 0:
        #     m = sum % 2
        #     if m == 1:
        #         arr.insert(0, '1')
        #     else:
        #         arr.insert(0, '0')

        #     sum = sum // 2
        
        # return ''.join(arr)