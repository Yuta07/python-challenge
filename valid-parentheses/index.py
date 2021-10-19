class Solution:
    def isValid(self, s: str) -> bool:
        valid_symbol = { "(": ")", "[": "]", "{": "}", }

        if len(s) == 1:
            return False
        
        if (s[0] not in valid_symbol.keys()):
            return False
        
        symbol_stack = [s[0]]

        for i in range(1, len(s)):
            if (i > len(s) - 1):
                return False

            if symbol_stack == []:
                if s[i] not in valid_symbol.keys():
                    return False
                else:
                    symbol_stack.append(s[i])
                
                continue

            if s[i] == valid_symbol[symbol_stack[-1]]:
                symbol_stack.pop()

                if (i == len(s) - 1):
                    if symbol_stack == []:
                        return True
                    else:
                        return False
                else:
                    continue
            else:
                if (i == len(s)):
                    return False
                else:
                  if s[i] not in valid_symbol.keys():
                    return False
                  else:
                      symbol_stack.append(s[i])