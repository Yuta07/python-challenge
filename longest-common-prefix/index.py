from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        minimum = min(strs)
        prefix_symbol = []
        
        for i in range(len(minimum)):
            prefix_symbol.append(strs[0][0:i + 1])

        result = ''

        if len(strs) == 1:
            result = strs[0]
                        
        for j in range(len(prefix_symbol)):
            for k in range(1, len(strs)):
                if strs[k].startswith(prefix_symbol[j]):
                    if k == len(strs) - 1:
                        result = prefix_symbol[j]
                    else:
                      continue
                else:
                    break

        return result