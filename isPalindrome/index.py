class Solution:
    def isPalindrome(self, x: int) -> bool:
        strCount = len(str(x))

        if (str(x)[0] == '-'):
            return False
        elif strCount == 1:
            return True
        else:            
            if strCount < 4:
                if str(x)[0] == str(x)[strCount - 1]:
                  return True
                else:
                  return False
            else:
                count = strCount // 2
                
                for i in range(count):
                    if str(x)[i] == str(x)[strCount - 1 - i]:
                        if i == count - 1:
                            return True
                        else:
                            continue
                    else:
                        return False